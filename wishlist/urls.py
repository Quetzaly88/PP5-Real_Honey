from django.urls import path
from .views import wishlist_view, add_to_wishlist, remove_from_wishlist, combined_view, add_to_cart_from_wishlist
from . import views

urlpatterns = [
    path('', wishlist_view, name='wishlist'),  # The path for the wishlist view
    path('add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:item_id>/', remove_from_wishlist,
         name='remove_from_wishlist'),
    path('combined/', combined_view, name='combined_view'),
    path('add_to_cart/<int:item_id>/', add_to_cart_from_wishlist,
         name='add_to_cart_from_wishlist'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]
