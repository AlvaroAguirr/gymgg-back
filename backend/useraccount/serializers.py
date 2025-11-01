from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from membership.serializers import MembershipSerializer
from membership.models import Membership

from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Para mostrar datos completos al leer


    # Para recibir solo el ID al crear/actualizar
    membership_id = serializers.PrimaryKeyRelatedField(
        queryset=Membership.objects.all(),
        source='membership',
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'membership', 'membership_id', 'date_pay', 'date_expiration']
        extra_kwargs = {
            'password': {'write_only': True},  # No mostrar la contraseña en las respuestas
            'is_active': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_superuser': {'write_only': True},
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # formzmiento de tipado 
        for field in ['is_active', 'is_staff', 'is_superuser']:
            if field in validated_data:
                value = validated_data[field]
                if isinstance(value, str):
                    validated_data[field] = value.lower() == 'true'

        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    


class UserSerializer2(serializers.ModelSerializer):
    membership_id = serializers.PrimaryKeyRelatedField(
        queryset=Membership.objects.all(),
        source='membership',
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id', 'name', 'email', 'password','membership',
            'membership_id', 'date_pay', 'date_expiration',
            'is_active', 'is_staff', 'is_superuser'
        ]
        read_only_fields = ['date_expiration']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_superuser': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        name = validated_data.pop('name', None)
        email = validated_data.pop('email', None)

        # Usar el manager personalizado para crear correctamente el usuario
        user = User.objects.create_user(
            name=name,
            email=email,
            password=password,
            **validated_data
        )

        return user



class UserSerializerEdit(serializers.ModelSerializer):
    # Para mostrar datos completos al leer


    # Para recibir solo el ID al crear/actualizar
    membership_id = serializers.PrimaryKeyRelatedField(
        queryset=Membership.objects.all(),
        source='membership',
        write_only=True
    )
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'membership_id', 'date_pay', 'date_expiration']
        read_only_fields = ['date_expiration']
   
 
 
# <<<<<<< HEAD
#     def get_name(self, obj):
#         return f"{obj.name}"
    


class CustomRegisterSerializer(RegisterSerializer):
    username = None  # <- Ocultamos este ca
    name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        print("CustomLoginSerializer.validate llamado")
        data = super().get_cleaned_data()
        data['name'] = self.validated_data.get('name', '')
        data['email'] = self.validated_data.get('email', '')
        data['password1'] = self.validated_data.get('password1', '')
        data['password2'] = self.validated_data.get('password2', '')
        return data
    



    def get_date_expiration(self, obj):
        if obj.date_expiration:
            return obj.date_expiration.strftime('%Y-%m-%d')
        return None

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    