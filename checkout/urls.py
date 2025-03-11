from django.urls import path
from .views import checkout_view, order_confirmation_view, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('', checkout_view, name='checkout_view'),
    path("order_confirmation/<str:order_number>/",
         order_confirmation_view, name='order_confirmation'),
    path("webhook/", webhook, name='webhook'),
    path("cache_checkout_data/", cache_checkout_data, name='cache_checkout_data'),
]
