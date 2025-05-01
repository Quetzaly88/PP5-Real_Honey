from django.db import models
from cloudinary.models import CloudinaryField


SIZE_CHOICES = [
    ('450g', '450gr'),
    ('600g', '600gr'),
    ('Standard', 'Standard')
]

CATEGORY_CHOICES = [
    ('honey', 'Honey'),
    ('bee_products', 'Bee Products'),
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    season = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    flavor_tones = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )
    image_2 = CloudinaryField(
        'image',
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='honey'
    )

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_sizes",
        default=1
    )
    size = models.CharField(
        max_length=100,
        choices=SIZE_CHOICES,
        blank=True,
        null=True
    )

    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        size_display = self.size if self.size else 'No Size'
        return f"{self.product.name} - {self.size} (${self.price})"
