from rest_framework import serializers

from .models import Product,Category


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoriesSerializer (serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'