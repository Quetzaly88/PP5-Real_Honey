from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishlistItem
from products.models import Product, ProductSize
from shopping_cart.models import CartItem


# Create your views here.
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size = request.POST.get('size')

    # Validate zize selection
    if not size:
        messages.error(request, "Please select size wishlist.")
        return redirect('product_detail', pk=product_id)

    # Ensure the sizes exists for the product
    # product_size = get_object_or_404(ProductSize, product=product, size=size)
    product_size_exists = Product.objects.filter(
        id=product_id, product_sizes__size=size).exists()
    if not product_size_exists:
        messages.error(request, "Invalid size selection.")
        return redirect('product_detail', pk=product_id)

    # Add the product to the wishlist
    WishlistItem.objects.get_or_create(
        product=product,
        user=request.user,
        size=size
    )
    messages.success(request, f"{product.name} ({size}) added to your wishlist!")
    return redirect('product_detail', pk=product_id)


@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(
        request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items}
    )


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(
        WishlistItem, id=item_id, user=request.user
        )
    wishlist_item.delete()
    messages.success(request, "Item removed.")
    return redirect('wishlist')


def login_redirect_view(request):
    messages.info(request, "Please log in to save products to your wishlist.")
    return redirect('account_login')


@login_required
def combined_view(request):
    # Fetch wishlist and cart items for the logged-in user
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate the total price of shopping cart items
    total_price = sum(item.get_total_price() for item in cart_items)

    return render(
        request,
        'wishlist/combined.html',
        {
            'wishlist_items': wishlist_items,
            'cart_items': cart_items,
            'total_price': total_price,
        }
    )


@login_required
def add_to_cart_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(
        WishlistItem, id=item_id, user=request.user)
    product = wishlist_item.product

    # Get the ProductSize from the wishlist item
    product_size = get_object_or_404(
        ProductSize, 
        product=wishlist_item.product,
        size=wishlist_item.size
    )

    # Add the product to the shopping cart
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product_size,
        size=product_size.size,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Remove the product from the wishlist
    wishlist_item.delete()

    messages.success(request, f"{product.name} added to your shopping cart!")
    return redirect('wishlist')
