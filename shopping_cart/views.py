from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CartItem
from products.models import Product, ProductSize
from django.conf import settings
from decimal import Decimal
from .models import Coupon
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

# Function to invalidate coupon on cart changes
def invalidate_coupon(request):
    if request.session.get('coupon_applied', False):
        request.session['coupon_applied'] = False
        request.session['coupon_discount'] = 0
        request.session['coupon_code'] = ''
        messages.info(request, "Cart updated - Please reapply your discount code")


# Function to get cart(logged-in and guest)
def get_cart_items(request):
    if request.user.is_authenticated:
        return CartItem.objects.filter(user=request.user)
    else:
        return request.session.get('cart', {})


# Function to add to cart
def add_to_cart(request, product_id):
    size = request.POST.get('size')
    product_size = get_object_or_404(
        ProductSize,
        product_id=product_id,
        size=size
    )

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product_size,
            size=size,
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart = request.session.get('cart', {})
        cart_key = f"{product_id}-{size}"
        if cart_key in cart:
            cart[cart_key]['quantity'] += 1
        else:
            cart[cart_key] = {
                'name': product_size.product.name,
                'size': size,
                'price': str(product_size.price),
                'quantity': 1,
            }
        request.session['cart'] = cart

    invalidate_coupon(request)

    messages.success(
        request, f"{product_size.product.name} ({size}) added to your cart.")
    return redirect('product_list')


# View Cart
@login_required
def cart_view(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(
            Decimal(item.get_total_price()) for item in cart_items
        )
    else:
        cart_items = request.session.get('cart', {})
        total_price = sum(
            Decimal(item['price']) * item['quantity']
            for item in cart_items.values()
        )

    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    standard_delivery_percentage = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)

    if total_price >= free_delivery_threshold:
        delivery_fee = Decimal('0')
        free_delivery_delta = Decimal('0')
    else:
        delivery_fee = (total_price * standard_delivery_percentage / Decimal('100')).quantize(Decimal('0.01'))
        free_delivery_delta = (free_delivery_threshold - total_price).quantize(Decimal('0.01'))

    coupon_discount = Decimal(request.session.get('coupon_discount', 0))
    grand_total = (total_price + delivery_fee - coupon_discount).quantize(Decimal('0.01'))

    # coupon_applied = request.session.get('coupon_applied', False)

    return render(request, 'shopping_cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'delivery_fee': delivery_fee,
        'free_delivery_delta': free_delivery_delta,
        'coupon_discount': coupon_discount,
        'grand_total': grand_total,
    })


# Remove from cart
@login_required
def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.delete()
    else:
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
        request.session['cart'] = cart

    messages.success(request, "Item removed from your cart.")
    invalidate_coupon(request)

    return redirect('cart')


# Update cart quantity
@login_required
def update_cart_quantity(request, item_id):
    if request.method == "POST":
        new_quantity = request.POST.get('quantity', "1")

        try:
            new_quantity = int(new_quantity)
            if new_quantity < 1:
                raise ValueError("Invalid quantity.")
        except ValueError:
            messages.error(request, "Invalid quantity.")
            return redirect('cart')

        if request.user.is_authenticated:
            cart_item = get_object_or_404(
                CartItem, id=item_id, user=request.user
            )
            if new_quantity > cart_item.product.stock:
                messages.error(request, f"Only {cart_item.product.stock} items available.")
                return redirect('cart')
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            cart = request.session.get('cart', {})
            if str(item_id) in cart:
                product_size = get_object_or_404(
                    ProductSize,
                    id=item_id
                )
                if new_quantity > product_size.product.stock:
                    messages.error(request, f"Only {product_size.stock} items available.")
                    return redirect('cart')
                cart[str(item_id)]['quantity'] = new_quantity
            else:
                messages.error(request, "Item not found in your cart.")
                return redirect('cart')

        invalidate_coupon(request)

        messages.success(request, "Cart updated.")
    return redirect('cart')


# Coupon validation
@login_required
def validate_coupon(request):
    if request.method == "POST":
        coupon_code = request.POST.get('coupon_code', '').strip()
        try:
            coupon = Coupon.objects.get(code__iexact=coupon_code, is_active=True)

            if coupon.expires_at and coupon.expires_at < now():
                messages.error(request, "Coupon has expired.")
                request.session['coupon_discount'] = 0
                request.session['coupon_applied'] = False
                return redirect('cart')

            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
                total_price = sum(
                    Decimal(item.get_total_price()) for item in cart_items
                )
            else:
                cart_items = request.session.get('cart', {})
                try:
                    total_price = sum(
                        Decimal(item['price']) * item['quantity']
                        for item in cart_items.values()
                    )
                except (KeyError, ValueError, TypeError, InvalidOperation):
                    messages.error(request, "Cart data is invalid.")
                    request.session['coupon_discount'] = 0
                    request.session['coupon_applied'] = False
                    return redirect('cart')

            if coupon.discount_type == 'fixed':
                discount_value = coupon.value
            else:
                discount_value = (total_price * coupon.value / Decimal('100')).quantize(Decimal('0.01'))

            request.session['coupon_discount'] = float(discount_value)
            request.session['coupon_applied'] = True
            request.session['coupon_code'] = coupon.code
            messages.success(request, "Coupon applied.")
        except Coupon.DoesNotExist:
            request.session['coupon_discount'] = 0
            request.session['coupon_applied'] = False
            request.session['coupon_code'] = ''
            messages.error(request, "Invalid coupon code.")
    return redirect('cart')
