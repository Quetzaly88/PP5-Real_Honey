import stripe
import json
import logging
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from products.models import ProductSize


# Set up logging
logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """
    Handle Stripe webhooks, including sending confirmation emails.
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject.strip(),
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
            fail_silently=False,
        )
        logger.info(f"Confirmation email sent to {cust_email}")

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event['data']['object']
        # payment_intent_id = intent.id
        metadata = intent.metadata

        # Extract order details from metadata
        order_number = metadata.get("order_number")
        save_info = metadata.get("save_info")
        username = metadata.get("username")

        # Get the charge object to retrieve billing details
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)
        # address_data = shipping_details.get("address", {})

        # Ensure order exists
        # order_number = metadata.get("order_number")
        order = Order.objects.filter(order_number=order_number).first()

        if order:
            order.payment_status = "Paid"
            order.save()
            return HttpResponse(
                content=f"Webhook received: {event['type']} | Order already exists",
                status=200,
            )
        else:
            #  Try to find user profile
            user_profile = None
            if username and username != "Guest":
                user_profile = UserProfile.objects.filter(user__username=username).first()

            # Create new order
            order = Order.objects.create(
                user_profile=user_profile,
                full_name=shipping_details.get("name", ""),
                email=metadata.get("email", ""),
                phone_number=billing_details.get("phone", ""),
                address=shipping_details.get("address", {}).get("line1", ""),
                town_or_city=shipping_details.get("address", {}).get("city", ""),
                country=shipping_details.get("address", {}).get("country", ""),
                total_cost=grand_total,
                final_price=grand_total,
                order_number=order_number,
            )

            # Save shipping info to profile if user opted to save info
            if save_info == "true" and user_profile:
                user_profile.full_name = order.full_name
                user_profile.email = order.email
                user_profile.phone_number = order.phone_number
                user_profile.address = order.address
                user_profile.town_or_city = order.town_or_city
                user_profile.country = order.country
                user_profile.save()

            order.save()
            self._send_confirmation_email(order)
            logger.info(f"Order {order_number} created successfully")

        return HttpResponse(
            content=f"Webhook received: {event['type']} | Order Created",
            status=200,
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """
        intent = event['data']['object']
        error_message = intent.get("last_payment_error", {}).get("message", "Unknown error")  # It’s good practice to log the error or return useful feedback.

        logger.error(f"Payment failed: {error_message}")
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200
        )
