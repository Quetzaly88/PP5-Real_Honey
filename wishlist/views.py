from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishlistItem
from products.models import Product 
from shopping_cart.models import CartItem 


# Create your views here.
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(product=product, user=request.user)
    messages.success(request, f"{product.name} added to your wishlist!")
    return redirect('product_list')


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

    return render(request,
        'wishlist/combined.html',
        {'wishlist_items': wishlist_items,
         'cart_items': cart_items,
         'total_price': total_price,
        }
        )