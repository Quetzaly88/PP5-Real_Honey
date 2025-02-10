from django.db import models
from django.contrib.auth.models import User
from products.models import Product 

# Create your models here.
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product') # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
