# Generated by Django 4.2.19 on 2025-02-14 09:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productsize_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wishlistitem',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='size',
            field=models.CharField(default='450g', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='wishlistitem',
            unique_together={('user', 'product', 'size')},
        ),
    ]
