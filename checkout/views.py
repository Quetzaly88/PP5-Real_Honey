import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from shopping_cart.models import CartItem
from products.models import ProductSize
from decimal import Decimal


def checkout_view(request):
    """
    Handles checkout form and order creation.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY # Initialize stripe

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

    # Create Stripe PaymentIntent
    payment_intent = stripe.PaymentIntent.create(
        amount=int(final_price * 100),
        currency='usd',
        metadata={'integration_check': "accept_a_payment"},
    )

    # Handle form submission
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save order first
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.total_cost = total_price
            order.delivery_fee = delivery_fee
            order.final_price = final_price
            order.save()

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
                request.session.pop('cart', None)

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
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': payment_intent.client_secret,  # Pass client secret to frontend
    }

    return render(request, 'checkout/checkout.html', context)
