# Generated by Django 4.2.19 on 2025-02-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_price_remove_product_sizes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
