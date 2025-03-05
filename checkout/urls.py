from django.urls import path
from .views import checkout_view, order_confirmation_view
from .webhooks import webhook

urlpatterns = [
    path('', checkout_view, name='checkout_view'),
    path("order_confirmation/<str:order_number>/",
         order_confirmation_view, name='order_confirmation'),
    path("webhook/", webhook, name='webhook'),
]
