from django.db import models

# Choices for category and size
CATEGORY_CHOICES = [
    ('spring', 'Spring'),
    ('summer', 'Summer'),
    ('autumn', 'Autumn'),
]

SIZE_CHOICES = [
    ('450g', '450gr'),
    ('600g', '600gr'),
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    season = models.CharField(max_length=100, blank=True, null=True)
    flavor_tones = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True)
    # New categories and sizes
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True,
    )
    size = models.CharField(
        max_length=100,
        choices=SIZE_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
