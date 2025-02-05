from django.urls import path
from .views import wishlist_view, add_to_wishlist   # Importing the views from the views.py file

urlpatterns = [
    path('add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('', wishlist_view, name='wishlist'),
]
