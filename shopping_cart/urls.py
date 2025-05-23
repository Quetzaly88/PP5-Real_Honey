from django.urls import path
from . import views
# from views import cart_view, add_to_cart, remove_from_cart, update_cart_quantity, validate_coupon, add_to_cart_with_size

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<str:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('validate_coupon/', views.validate_coupon, name='validate_coupon'),
]
