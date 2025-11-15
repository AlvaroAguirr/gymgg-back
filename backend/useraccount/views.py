from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated



from membership.serializers import MembershipSerializer
from .models import User
from .serializers import UserSerializer, UserSerializerEdit, UserSerializer2,MyTokenObtainPairSerializer, UserSerializerAdmin



from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response
from rest_framework import status


class UserListApi(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    
    
class UserCreateApi(CreateAPIView):
    serializer_class = UserSerializerAdmin
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        current_user = request.user
        print(current_user)
        print(current_user.is_superuser)
        # Si el usuario es superadmin → crea recepcionistas
        if current_user.is_superuser:
            role = request.data.get('role', 'recepcionista')
            user_data = request.data.copy()
            print(f"user data {user_data}")
            if role == 'recepcionista':
                user_data['is_staff'] = True
                user_data['is_active'] = True
                user_data['is_superuser'] = False
                print(user_data)
            else:
                return Response({'detail': 'Rol inválido para superadmin.'}, status=status.HTTP_400_BAD_REQUEST)
            
        
        # Si el usuario es recepcionista → crea usuarios comunes
        elif current_user.is_staff:
            user_data = request.data.copy()
            user_data['is_staff'] = False
            user_data['is_superuser'] = False
            user_data['is_active'] = False  # no puede acceder al sistema

         

        else:
            return Response({'detail': 'No tienes permisos para crear usuarios.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=user_data)
        # serializer = self.serializer_class(data=user_data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación:", serializer.errors)  # <--- Aquí
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateApiRecep(CreateAPIView):
    serializer_class = UserSerializer2
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        current_user = request.user
        print(current_user)
        print(current_user.is_superuser)
        # Si el usuario es superadmin → crea recepcionistas
        if current_user.is_superuser:
            role = request.data.get('role', 'recepcionista')
            user_data = request.data.copy()
            print(f"user data {user_data}")
            if role == 'recepcionista':
                user_data['is_staff'] = True
                user_data['is_active'] = True
                user_data['is_superuser'] = False
                print(user_data)
            else:
                return Response({'detail': 'Rol inválido para superadmin.'}, status=status.HTTP_400_BAD_REQUEST)
            
        
        # Si el usuario es recepcionista → crea usuarios comunes
        elif current_user.is_staff:
            user_data = request.data.copy()
            user_data['is_staff'] = False
            user_data['is_superuser'] = False
            user_data['is_active'] = False  # no puede acceder al sistema

         

        else:
            return Response({'detail': 'No tienes permisos para crear usuarios.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=user_data)
        # serializer = self.serializer_class(data=user_data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación:", serializer.errors)  # <--- Aquí
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# ver objeto especifico
class UserDetailApi(RetrieveAPIView):
    serializer_class = UserSerializer

# delete objeto especifico
class UserDeleteApi(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

class UserUpdateApi(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerEdit

class MembershipListApi(ListAPIView):
    serializer_class = MembershipSerializer
    def get_queryset(self):
        return MembershipSerializer.objects.all()