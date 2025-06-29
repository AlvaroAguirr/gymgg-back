# views.py

from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from .models import Sales
from .serializers import SaleSerializer

class SaleListApi(ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer

class SaleCreateApi(CreateAPIView):
    serializer_class = SaleSerializer

class SaleDetailApi(RetrieveAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer

class SaleUpdateApi(UpdateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer

class SaleDeleteApi(DestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer
