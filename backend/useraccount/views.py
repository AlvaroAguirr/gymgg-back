from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)

from membership.serializers import MembershipSerializer
from .models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status


class UserListApi(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
class UserCreateApi(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación:", serializer.errors)  # <--- Aquí
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ver objeto especifico
class UserDetailApi(RetrieveAPIView):
    serializer_class = UserSerializer

# delete objeto especifico
class UserDeleteApi(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

class UserUpdateApi(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MembershipListApi(ListAPIView):
    serializer_class = MembershipSerializer
    def get_queryset(self):
        return MembershipSerializer.objects.all()