# serializers.py

from rest_framework import serializers
from .models import Sales, SaleItem
from products.models import Product

class SaleItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name_product')

    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['total_price']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Sales
        fields = ['id', 'created_at', 'items', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sales.objects.create(**validated_data)
        for item_data in items_data:
            SaleItem.objects.create(sale=sale, **item_data)
        return sale
