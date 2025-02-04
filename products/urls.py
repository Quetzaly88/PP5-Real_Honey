from django.urls import path
from . import views
from .views import product_list, product_detail

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]