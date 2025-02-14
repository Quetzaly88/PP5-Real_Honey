from django.db import models
from django.contrib.auth.models import User
from products.models import Product 

# Create your models here.
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, default='450g')  # size required

    class Meta:
        unique_together = ('user', 'product', 'size')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.size})"
