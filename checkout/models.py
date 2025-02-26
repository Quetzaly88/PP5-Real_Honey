import uuid
from django.db import models
from django.conf import settings
from products.models import ProductSize
from shopping_cart.models import Coupon


class Order(models.Model):
    order_number = models.CharField(
        max_length=32, null=False, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

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

    def _generate_order_number(self):
        """Generates unique order number, 10 digits"""
        return str(uuid.uuid4().hex[:10]).upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()

        # ensure finnal_price is calculated (total - discount + delivery)
        self.final_price = max(self.total_cost - self.discount_amount + self.delivery_fee, 0)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - {self.full_name}"


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='line_items')
    product = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        """discount applies dinamically when a coupon is applied"""
        if not self.order_number:
            self.order_number = self._generate_order_number()

        # ensure discount_amount is updated dynamically if a coupon is applied
        if self.applied_coupon:
            if self.applied_coupon.discount_type == 'fixed':
                self.discount_amount = self.applied_coupon.value
            elif self.applied_coupon.discount_type == 'percent':
                self.discount_amount = (self.total_cost * self.applied_coupon.value) / 100

        # final price calculation
        self.final_price = max(self.total_cost - self.discount_amount + self.delivery_fee, 0)

        super().save(*args, **kwargs)

    @property
    def line_total(self):
        """Calculates the total price for this line item"""
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.product.name} - {self.quantity} x ${self.price}"
