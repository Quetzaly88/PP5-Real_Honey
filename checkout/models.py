import uuid
from django.db import models
from django.conf import settings
from products.models import ProductSize
from shopping_cart.models import Coupon
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(
        max_length=32, unique=True, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
    )

    # shipping info
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)

    # pricing and discounts
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    #  Coupon reference
    applied_coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
    )

    # User profile
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
    )

    def _generate_order_number(self):
        """Generates unique order number, 10 digits"""
        return str(uuid.uuid4().hex[:10]).upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()

        # save the order first
        super().save(*args, **kwargs)

        # Recalculate total_cost
        self.total_cost = sum([item.line_total for item in self.line_items.all()]) if self.line_items.exists() else 0

        # ensure final_price is calculated (total - discount + delivery)
        self.final_price = max(self.total_cost - self.discount_amount + self.delivery_fee, 0)

        super().save(update_fields=['total_cost', 'final_price'])

    def __str__(self):
        return f"Order {self.order_number} - {self.full_name}"


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='line_items')
    product = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=True, default=0.00)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.00)

    def save(self, *args, **kwargs):
        """
        Ensure total_cost is calculated after order instance is saved
        """

        if self.price is None and self.product:
            self.price = self.product.price  # Use product price if not manually set

        self.line_total = self.price * self.quantity

        super().save(*args, **kwargs)

        if self.order:
            self.order.save()

    def __str__(self):
        return f"{self.product.product.name} - {self.quantity} x ${self.price}"
