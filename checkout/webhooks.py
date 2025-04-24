import stripe
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe
    """
    # Setup Stripe API key and Webhook secret
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        print("Invalid payload")
        return HttpResponse(status=400)  # Invalid payload
    except stripe.error.SignatureVerificationError:
        print("Invalid signature")
        return HttpResponse(status=400)  # Invalid signature

    # Set up webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to their handlers
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Get the event type from Stripe
    event_type = event['type']

    # Log the received event
    print(f"Webhook received: {event_type}")

    # If there's a handler for it, use it. Otherwise, use the generic one
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)

    print("Webhook processed successfully")

    return response
