from django.urls import path
from . import views
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<str:category>/', views.product_list,
         name='product_category'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
