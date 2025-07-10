from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)
from .models import Product, Category
from .serializers import ProductoSerializer, CategoriesSerializer

class ProductoListApi(ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        return Product.objects.all()
    
class ProductoCreateApi(CreateAPIView):
    serializer_class = ProductoSerializer


# ver objeto especifico
class ProductoDetailApi(RetrieveAPIView):
    serializer_class = ProductoSerializer

# delete objeto especifico
class ProductoDeleteApi(DestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = Product.objects.filter()

class ProductoUpdateApi(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer



class CategoryListApi(ListAPIView):
    serializer_class = CategoriesSerializer
    def get_queryset(self):
        return Category.objects.all()