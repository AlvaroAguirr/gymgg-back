# Generated by Django 5.2.3 on 2025-06-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='quantity',
        ),
        migrations.AddField(
            model_name='sales',
            name='id_products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
