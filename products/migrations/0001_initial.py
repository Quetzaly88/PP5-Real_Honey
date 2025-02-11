# Generated by Django 4.2.19 on 2025-02-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('season', models.CharField(blank=True, max_length=100, null=True)),
                ('flavor_tones', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('avaiable_sizes', models.CharField(blank=True, help_text='Comma-separated sizes, e.g., 450g,600g', max_length=100, null=True)),
            ],
        ),
    ]
