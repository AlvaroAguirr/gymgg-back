from rest_framework import serializers

from .models import Product,Category


class ProductoSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name_category',
        queryset=Category.objects.all()
    )
    class Meta:
        model = Product
        fields = [
            'id',
            'name_product',
            'price_product',
            'description',
            'stock',
            'image_url',
            'category',
        ]


class CategoriesSerializer (serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'