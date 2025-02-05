from django.db import models
from django.contrib.auth.models import User 
from products.models import Product 

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

    def get_total_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"