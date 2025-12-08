from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated

from membership.serializers import MembershipSerializer
from .models import User
from .serializers import (
    UserSerializer, 
    UserSerializerEdit, 
    UserSerializer2,
    MyTokenObtainPairSerializer, 
    UserSerializerAdmin,
    UserSerializerWithRole  # Asegúrate de importarlo
)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action


class UserListApi(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    

class UserCreateApi(CreateAPIView):
    serializer_class = UserSerializerWithRole  # ← CAMBIADO de UserSerializerAdmin
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        current_user = request.user
        print(current_user.email)
        print(current_user.is_superuser)
        
        user_data = request.data.copy()
        role = user_data.get('role', 'user')
        
        print(f"user data {user_data}")
        
        # Validar permisos según el usuario actual
        if current_user.is_superuser:
            # El superadmin puede crear cualquier tipo de usuario
            pass  # user_data ya tiene el rol correcto
            
        elif current_user.is_staff:
            # El recepcionista solo puede crear usuarios normales
            if role != 'user':
                return Response({
                    'detail': 'Como recepcionista solo puedes crear usuarios normales.'
                }, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({
                'detail': 'No tienes permisos para crear usuarios.'
            }, status=status.HTTP_403_FORBIDDEN)

        # Crear usuario con el serializer que maneja roles
        serializer = self.serializer_class(data=user_data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'id': str(user.id),
                'email': user.email,
                'name': user.name,
                'role': user.role,
                'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateApiRecep(CreateAPIView):
    serializer_class = UserSerializerWithRole  # ← CAMBIADO de UserSerializer2
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        current_user = request.user
        print(current_user.email)
        print(current_user.is_superuser)
        
        user_data = request.data.copy()
        role = user_data.get('role', 'user')
        
        print(f"user data {user_data}")
        
        # Validar permisos
        if current_user.is_superuser:
            pass  # Puede crear cualquier tipo
            
        elif current_user.is_staff:
            # Solo puede crear usuarios normales
            if role != 'user':
                return Response({
                    'detail': 'Como recepcionista solo puedes crear usuarios normales.'
                }, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({
                'detail': 'No tienes permisos para crear usuarios.'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=user_data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'id': str(user.id),
                'email': user.email,
                'name': user.name,
                'role': user.role,
                'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación:", serializer.errors)
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
      
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializerWithRole
        return UserSerializer 
    
    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = UserSerializerWithRole(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)