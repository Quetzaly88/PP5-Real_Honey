from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    """
    Allows adding order line items directly in the admin.
    """
    model = OrderLineItem
    readonly_fields = ('line_total',)
    extra = 1  # Allow adding items

    def calculated_line_total(self, obj):
        """
        Calculates total price per line item. 
        """
        if obj and obj.price is not None and obj.quantity is not None:
            return obj.line_total
        return 0

    calculated_line_total.short_description = 'Total Price'


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

    def save_model(self, request, obj, form, change):
        """
        Ensure total cost is updated when saving
        """
        obj.total_cost = sum([item.line_total for item in obj.line_items.all()]) if obj.line_items.exists() else 0
        obj.final_price = max(obj.total_cost - obj.discount_amount + obj.delivery_fee, 0)
        super().save_model(request, obj, form, change)


@admin.register(OrderLineItem)
class OrderLineItemAdmin(admin.ModelAdmin):
    """
    Admin view for managing order line items.
    """
    list_display = (
        'order',
        'product',
        'quantity',
        'price',
        'calculated_line_total',
    )
    search_fields = (
        'order__order_number',
        'product__product__name',
    )
    list_filter = (
        'order__date_created',
    )

    readonly_fields = ('calculated_line_total',)

    def calculated_line_total(self, obj):
        """
        Calculates total price per line item. 
        """
        if obj and obj.price is not None and obj.quantity is not None:
            return obj.line_total
        return 0
    
    calculated_line_total.short_description = 'Total Price'
