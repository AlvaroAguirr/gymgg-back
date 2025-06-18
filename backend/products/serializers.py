from rest_framework import serializers

from .models import Product


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name_product', 'price_product', 'description', 'stock', 'category')