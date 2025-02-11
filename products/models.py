from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    season = models.CharField(max_length=100, blank=True, null=True) #make season optional
    flavor_tones = models.CharField(max_length=200, blank=True, null=True) #make flavor_tones optional
    category = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True) #make image optional
    avaiable_sizes = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Comma-separated sizes, e.g., 450g,600g"
    )

    def get_sizes(self):
        if self.avaiable_sizes:
            return self.avaiable_sizes.split(",")
        return []   

    def __str__(self):
        return self.name