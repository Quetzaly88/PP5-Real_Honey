import stripe
from django.http import HttpResponse
from django.conf import settings
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from products.models import ProductSize
import json


"""
This file will handle Stripe webhooks.
Listens for webhooks events, handles successful payments as
failed payments.
"""


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

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

        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200
        )
