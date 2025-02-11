# Generated by Django 4.2.19 on 2025-02-11 17:03

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
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('season', models.CharField(blank=True, choices=[('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('standard', 'Standard')], max_length=100, null=True)),
                ('flavor_tones', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.CharField(blank=True, choices=[('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('standard', 'Standard')], max_length=100, null=True)),
                ('size', models.CharField(blank=True, choices=[('450g', '450gr'), ('600g', '600gr')], max_length=100, null=True)),
            ],
        ),
    ]
