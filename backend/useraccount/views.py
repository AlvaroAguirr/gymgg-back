from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)
from .models import User
from .serializers import UserSerializer

class UserListApi(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()