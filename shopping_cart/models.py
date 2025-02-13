from django.db import models
from django.contrib.auth.models import User
from products.models import ProductSize


# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, default='450g')
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.product.name} - {self.size} ({self.quantity})"
