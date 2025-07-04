from rest_framework import serializers

from .models import Product


class ProductoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'