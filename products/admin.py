from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'size', 'season')
    list_filter = ('category', 'size', 'season')
    search_fields = ('name', 'description')

    