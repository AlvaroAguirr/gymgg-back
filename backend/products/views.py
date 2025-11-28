from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated 
from rest_framework.permissions import AllowAny




from .models import Product, Category
from .serializers import ProductoSerializer, CategoriesSerializer
# from .utils import upload_image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# class UploadImageApi(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, *args, **kwargs):
#         file = request.data.get('file')
#         if not file:
#             return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
#         
#         try:
#             image_url = upload_image(file)
#             return Response({'url': image_url}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





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
    permission_classes = [IsAuthenticated] 


class ProductoUpdateApi(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  



class CategoryListApi(ListAPIView):
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.all()
    
    
class CategoryCreateApi(CreateAPIView):
    serializer_class = CategoriesSerializer
    permission_classes=[IsAuthenticated]
