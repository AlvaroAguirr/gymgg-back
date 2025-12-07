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
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # Limpieza de valores (evita errores de Excel)
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        # Validaciones manuales
        required_fields = ["name_product", "price_product", "stock", "category"]

        for field in required_fields:
            if not data.get(field):
                return Response(
                    {"error": f"El campo '{field}' está vacío o no existe."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Validar numéricos
        try:
            float(data["price_product"])
        except:
            return Response(
                {"error": "El precio no es un número válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            int(data["stock"])
        except:
            return Response(
                {"error": "El stock no es un número válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validar categoría existente
        if not Category.objects.filter(name_category=data["category"]).exists():
            return Response(
                {"error": f"La categoría '{data['category']}' no existe."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Crear producto
        return super().create(request, *args, **kwargs)



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

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        data = request.data.copy()

        # Si no mandan imagen, conserva la anterior
        if "image_url" not in data or data["image_url"] in ["", None, "null"]:
            data["image_url"] = instance.image_url

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)




class CategoryListApi(ListAPIView):
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.all()
    
    
class CategoryCreateApi(CreateAPIView):
    serializer_class = CategoriesSerializer
    permission_classes=[IsAuthenticated]
