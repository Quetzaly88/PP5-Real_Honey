from django.urls import path
from . import views
from .views import product_list, product_detail, add_product, edit_product, delete_product

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<str:category>/', views.product_list,
         name='product_category'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
]
