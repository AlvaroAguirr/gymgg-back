from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated 
from rest_framework.permissions import AllowAny




from .models import Product, Category
from .serializers import ProductoSerializer, CategoriesSerializer




class ProductoListApi(ListAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Product.objects.all()
    
class ProductoCreateApi(CreateAPIView):
    serializer_class = ProductoSerializer
    permission_classes=[IsAuthenticated]



# ver objeto especifico
class ProductoDetailApi(RetrieveAPIView):
    serializer_class = ProductoSerializer
    permission_classes=[IsAuthenticated]


# delete objeto especifico
class ProductoDeleteApi(DestroyAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # 👈 Protegida


class ProductoUpdateApi(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # 👈 Protegida



class CategoryListApi(ListAPIView):
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]
  # 👈 Protegida

    def get_queryset(self):
        return Category.objects.all()