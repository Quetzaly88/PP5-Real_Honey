import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order, OrderLineItem
from shopping_cart.models import CartItem
from products.models import ProductSize
from decimal import Decimal

from django.http import JsonResponse
from django.views.decorators.csfr import csrf_exempt


def checkout_view(request):
    """
    Handles checkout form and order creation.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY  # Initialize stripe

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = request.session.get('cart', {})

    # Redirect if cart is empty
    if not cart_items or (request.user.is_authenticated and not cart_items.exists()):
        messages.error(request, "Your cart is empty.")
        return redirect('product_list')

    # Calculate total price
    if request.user.is_authenticated:
        total_price = sum(item.get_total_price() for item in cart_items)
    else:
        total_price = sum(Decimal(item['price']) * item['quantity'] for item in cart_items.values())

    # Delivery fee logic
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    standard_delivery_percentage = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)

    if total_price >= free_delivery_threshold:
        delivery_fee = Decimal('0')
        free_delivery_delta = Decimal('0')
    else:
        delivery_fee = (total_price * standard_delivery_percentage / Decimal('100')).quantize(Decimal('0.01'))
        free_delivery_delta = (free_delivery_threshold - total_price).quantize(Decimal('0.01'))

    final_price = (total_price + delivery_fee).quantize(Decimal('0.01'))

    #  Create payment with metadata
    metadata = {
        'integration_check': 'accept_a_payment',
        'user_id': request.user.id if request.user.is_authenticated else "Guest",
        'cart_backup': str(cart_items),  # Store cart for later
        'email': request.user.email if request.user.is_authenticated else "",
    }

    # Create Stripe PaymentIntent
    payment_intent = stripe.PaymentIntent.create(
        amount=int(final_price * 100),
        currency='usd',
        metadata={'integration_check': "accept_a_payment"},
    )

    # Store the PaymentIntent ID in the session (used for webhook validation)
    request.session['payment_intent_id'] = payment_intent.id

    # Handle form submission
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save order first
            order = form.save(commit=False)

            # Attach user profile if authenticated
            if request.user.is_authenticated:
                user_profile, created = UserProfile.objects.get_or_create(user=request.user)
                order.user_profile = user_profile

            order.total_cost = total_price
            order.delivery_fee = delivery_fee
            order.final_price = final_price
            order.county = request.POST.get('county', '')
            order.save()

            # Save shipping info if user checked "save info"
            if request.user.is_authenticated and 'save_info' in request.POST:
                user_profile.full_name = form.cleaned_data['full_name']
                user_profile.email = form.cleaned_data['email']
                user_profile.phone_number = form.cleaned_data['phone_number']
                user_profile.address = form.cleaned_data['address']
                user_profile.town_or_city = form.cleaned_data['town_or_city']
                user_profile.postcode = form.cleaned_data['postcode']
                user_profile.county = form.cleaned_data['county']
                user_profile.country = form.cleaned_data['country']
                user_profile.save()

            # Create order line items
            if request.user.is_authenticated:
                for item in cart_items:
                    OrderLineItem.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.product.price,
                    )
                cart_items.delete()

            else:
                for key, item in cart_items.items():
                    product_size = get_object_or_404(ProductSize, id=int(key))
                    OrderLineItem.objects.create(
                        order=order,
                        product=product_size,
                        quantity=item['quantity'],
                        price=Decimal(item['price']),
                    )
                request.session['cart'] = {}

            messages.success(request, 'Order successfully placed.')
            return redirect('order_confirmation', order_number=order.order_number)

        else:
            messages.error(request, 'Error processing order. Please check your information.')

    else:
        form = OrderForm()

    # Render checkout page
    context = {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price,
        'delivery_fee': delivery_fee,
        'final_price': final_price,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY if settings.STRIPE_PUBLIC_KEY else '',
        'client_secret': payment_intent.client_secret if payment_intent else '',   # Pass client secret to frontend
    }

    return render(request, 'checkout/checkout.html', context)


def order_confirmation_view(request, order_number):
    """
    Displays order confirmation page.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully placed. Your order number is {order_number}.')

    context = {'order': order}

    return render(request, 'checkout/order_confirmation.html', context)


@csrf_exempt
def cache_checkout_data(request):
    """
    Temporary store data before payment is confirmed.
    """
    try:
        request.session['checkout_data'] = request.POST
        return JsonResponse({"message": "Checkout data successfully saved."}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
