from django.urls import path
from .views import profile_view, order_detail_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('order/<order_number>/', order_detail_view, name='order_detail'),
]
