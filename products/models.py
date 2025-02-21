from django.db import models


SIZE_CHOICES = [
    ('450g', '450gr'),
    ('600g', '600gr'),
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
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )
    image_2 = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )
    # New field for featured products
    is_featured = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)

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
    )

    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size} (${self.price})"
