from django.contrib import admin
from .models import Coupon

# Register your models here.
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'value', 'is_active', 'expires_at']
    search_fields = ['code']
    list_filter = ['discount_type', 'is_active', 'expires_at']
