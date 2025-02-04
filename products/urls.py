from django.urls import path
from . import views
from .views import product_list, product_detail 

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
]