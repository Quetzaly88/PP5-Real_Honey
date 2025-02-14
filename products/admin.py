from django.contrib import admin
from .models import Product, ProductSize


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1 # Allows adding size price combinations directly in admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'season')
    search_fields = ('name', 'description')
    inlines = [ProductSizeInline]
    list_filter = ('season',)
