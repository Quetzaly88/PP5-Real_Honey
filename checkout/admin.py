from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    """
    Allows adding order line items directly in the admin.
    """
    model = OrderLineItem
    readonly_fields = ('line_total',)
    extra = 1  # Allow adding items

    def line_total(self, obj):
        """
        Calculates total price per line item. 
        """
        return obj.line_total
    
    line_total.short_description = 'Total Price'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin view for managing orders.
    """
    list_display = (
        'order_number',
        'full_name',
        'email',
        'total_cost',
        'final_price',
        'date_created',
    )
    list_filter = (
        'date_created',
        'country'
    )
    search_fields = (
        'order_number',
        'full_name',
        'email'
    )

    readonly_fields = (
        'order_number',
        'total_cost',
        'discount_amount',
        'delivery_fee',
        'final_price',
        'date_created'
    )

    inlines = [OrderLineItemInline]  # Show order items inside the order admin page. 

    #  More organized than just fields. 
    fieldsets = (
        ('Order Details', {
            'fields': ('order_number', 'user', 'date_created')
        }),
        ('Customer Info', {
            'fields': ('full_name', 'email', 'phone_number', 'address', 'town_or_city', 'postcode', 'county', 'country')
        }),
        ('Pricing and Discounts', {
            'fields': ('total_cost', 'discount_amount', 'delivery_fee', 'final_price', 'applied_coupon')
        }),
    )
