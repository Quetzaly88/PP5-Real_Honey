from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CartItem
from products.models import ProductSize


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
        # logged in user saved to database.
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

    messages.success(
        request, f"{product_size.product.name} ({size}) added to your cart.")
    return redirect('product_list')


# View Cart
def cart_view(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)
    else:
        cart_items = request.session.get('cart', {})
        total_price = sum(
            float(item['price']) * item['quantity']
            for item in cart_items.values())

    return render(request, 'shopping_cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


# Remove from cart
def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        # Remove item from the database for logged-in users
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.delete()
    else:
        # Remove item from the session for guest users
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
        request.session['cart'] = cart

    messages.success(request, "Item removed from your cart.")
    return redirect('cart')


# Update cart quantity
def update_cart_quantity(request, item_id):
    if request.method == "POST":
        new_quantity = int(request.POST.get("quantity", 1))

        if request.user.is_authenticated:
            cart_item = get_object_or_404(
                CartItem, id=item_id, user=request.user)
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            cart = request.session.get('cart', {})
            if str(item_id) in cart:
                cart[str(item_id)]['quantity'] = new_quantity
            request.session['cart'] = cart

        messages.success(request, "Cart updated.")
    return redirect('cart')
