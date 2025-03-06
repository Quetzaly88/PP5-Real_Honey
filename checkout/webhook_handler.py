import stripe
from django.http import HttpResponse
from .models import Order

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
        pid = intent.id
        metadata = intent.metadata

        # Get the charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        #  Extract billing and shipping details
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Ensure order exists
        order_number = metadata.get("order_number")
        order = Order.objects.filter(order_number=order_number).first()

        if order:
            order.payment_status = "Paid"
            order.save()
            return HttpResponse(
                content=f"Webhook received: {event['type']} | Order already exists",
                status=200,
            )
        else:
            #  Create the order if it doesn't exist
            order = Order.objects.create(
                full_name=shipping_details.get("name", ""),
                email=metadata.get("email", ""),
                phone_number=billing_details.get("phone", ""),
                address=shipping_details.get("address", {}).get("line1", ""),
                town_or_city=shipping_details.get("adress", {}).get("city", ""),
                country=shipping_details.get("adress", {}).get("country", ""),
                total_cost=grand_total,
                final_price=grand_total,
                order_number=order_number,
            )

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
