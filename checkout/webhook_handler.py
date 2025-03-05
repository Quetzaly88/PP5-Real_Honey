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
        order_number = intent.get("metadata", {}).get("order_number")

        if not order_number:
            return HttpResponse(
                content="No order number in metadata",
                status=400,
            )

        order = Order.objects.filter(order_number=order_number).first()

        if order:
            order.payment_status = "Paid"
            order.save()
            return HttpResponse(
                content=f"Webhook received: {event['type']}",
                status=200,
            )
        else:
            # if order doesn't exist, handle accordingly
            return HttpResponse(
                content="Order not found in database.",
                status=400,
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
