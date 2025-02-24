from django.db import models
from django.contrib.auth.models import User
from products.models import ProductSize


class CartItem(models.Model):
    product = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, default='450g')
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.product.name} - {self.size} ({self.quantity})"


# coupon model
class Coupon(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('fixed', 'Fixed'),
        ('percent', 'Percent'),
    ]

    code = models.CharField(max_length=50, unique=True)  # unique coupon code
    value = models.DecimalField(max_digits=6, decimal_places=2)  # coupon value
    discount_type = models.CharField(
        max_length=10,
        choices=DISCOUNT_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)  # coupon status
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.code
