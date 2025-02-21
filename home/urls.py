# from django.contrib import admin
from django.urls import path
from . import views
from .views import home_view

urlpatterns = [
    path('', views.index, name='home'),
    path('', home_view, name='home'),
]
