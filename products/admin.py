from django.contrib import admin
from .models import Product, ProductSize


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'season')
    list_filter = ('category', 'season')
    search_fields = ('name', 'description')
    filter_horizontal = ('sizes',)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
