from rest_framework import serializers

from products.serializers import ProductoSerializer
from .models import Sales, SaleItem
from useraccount.models import User
from products.models import Product

class SaleItemSerializer(serializers.ModelSerializer):
    product = ProductoSerializer(read_only=True)  # Muestra info completa al hacer GET
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',  # asigna al campo product del modelo
        write_only=True    # solo para POST/PUT
    )
    name_product = serializers.ReadOnlyField(source='product.name_product')

    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'product_id', 'name_product', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['total_price']
class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Sales
        fields = ['id', 'created_at', 'user', 'items', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        print("items_data en create:", items_data)
        sale = Sales.objects.create(**validated_data)
        for item_data in items_data:
            print("item_data individual:", item_data)
            quantity = item_data['quantity']
            unit_price = item_data['unit_price']
            total_price = quantity * unit_price
            SaleItem.objects.create(
                sale=sale,
                product=item_data['product'],
                quantity=quantity,
                unit_price=unit_price,
                total_price=total_price
            )
        return sale




# from rest_framework import serializers

# from useraccount.models import User
# from useraccount.serializers import UserSerializer
# from .models import Sales, SaleItem
# from products.models import Product

# class UserNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'name']  # solo lo que quieres mostrar aquí

# class SaleItemSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     name_product = serializers.ReadOnlyField(source='product.name_product')  # CORREGIDO aquí

#     class Meta:
#         model = SaleItem
#         fields = ['id', 'product', 'name_product', 'quantity', 'unit_price', 'total_price']
#         read_only_fields = ['total_price']

# class SaleSerializer(serializers.ModelSerializer):
#     items = SaleItemSerializer(many=True, source='productos')  # related_name en modelo SaleItem
#     total_price = serializers.ReadOnlyField()
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     class Meta:
#         model = Sales
#         fields = ['id', 'created_at', 'user', 'items', 'total_price']

#     def create(self, validated_data):
#         items_data = validated_data.pop('productos')
#         sale = Sales.objects.create(**validated_data)
#         for item_data in items_data:
#             SaleItem.objects.create(sale=sale, **item_data)
#         return sale
