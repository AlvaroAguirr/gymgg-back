# serializers.py

from rest_framework import serializers

from useraccount.models import User
from useraccount.serializers import UserSerializer
from .models import Sales, SaleItem
from products.models import Product

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']  # solo lo que quieres mostrar aquí

class SaleItemSerializer(serializers.ModelSerializer):
    name_product = serializers.ReadOnlyField(source='product.name_product')

    class Meta:
        model = SaleItem
        fields = ['id', 'name_product', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['total_price']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, source='productos', read_only=True)
    total_price = serializers.ReadOnlyField()
    user = UserNameSerializer(read_only=True)
    user_email = serializers.StringRelatedField()

    class Meta:
        model = Sales
        fields = ['id', 'created_at', 'user', 'user_email', 'items', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sales.objects.create(**validated_data)
        for item_data in items_data:
            SaleItem.objects.create(sale=sale, **item_data)
        return sale
