# Generated by Django 4.2.19 on 2025-02-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productsize_remove_product_size_product_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='season',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
