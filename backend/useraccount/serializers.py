from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from membership.models import Membership

from .models import User

class UserSerializer(serializers.ModelSerializer):
    membership_id = serializers.PrimaryKeyRelatedField(
        queryset=Membership.objects.all(),
        source='membership',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = User
        fields = [
            'id', 'name', 'email', 'password', 
            'role',  # ← ASEGÚRATE DE QUE ESTÉ AQUÍ
            'membership', 'membership_id', 
            'date_pay', 'date_expiration', 
            'is_active'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user 


class UserSerializerAdmin(serializers.ModelSerializer):
 

    class Meta:
        model = User
        fields = [
            'id', 'name', 'email', 'password',
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Información extra en el payload del token
        token['name'] = user.name
        token['email'] = user.email
        token['role'] = user.role  # ← NUEVO: Agregar esto
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['is_active'] = user.is_active
        token['membership'] = str(user.membership.id) if user.membership else None

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        user = self.user 

        data['name'] = self.user.name
        data['email'] = self.user.email
        data['role'] = self.user.role  # ← NUEVO: Agregar esto
        data['membership'] = str(user.membership.id) if user.membership else None
        data['is_staff'] = self.user.is_staff
        data['is_superuser'] = self.user.is_superuser
        data['is_active'] = self.user.is_active

        return data


class UserSerializerWithRole(serializers.ModelSerializer):
    membership_id = serializers.PrimaryKeyRelatedField(
        queryset=Membership.objects.all(),
        source='membership',
        write_only=True,
        required=False,
        allow_null=True
    )
    role_display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'name', 'email', 'password', 'role', 'role_display',
            'membership', 'membership_id', 'date_pay', 'date_expiration',
            'is_active', 'is_staff', 'is_superuser'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
        }

    def get_role_display(self, obj):
        """Retorna el nombre del rol en español"""
        role_map = {
            'admin': 'Administrador',
            'receptionist': 'Recepcionista',
            'user': 'Usuario'
        }
        return role_map.get(obj.role, 'Usuario')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.get('role', 'user')
        
        # Crear usuario según el rol
        if role == 'admin':
            user = User.objects.create_superuser(
                email=validated_data.get('email'),
                password=password,
                name=validated_data.get('name'),
                membership=validated_data.get('membership'),
                date_pay=validated_data.get('date_pay')
            )
        elif role == 'receptionist':
            user = User.objects.create_recepcionist(
                email=validated_data.get('email'),
                password=password,
                name=validated_data.get('name'),
                membership=validated_data.get('membership'),
                date_pay=validated_data.get('date_pay')
            )
        else:
            user = User.objects.create_user(
                email=validated_data.get('email'),
                password=password,
                name=validated_data.get('name'),
                membership=validated_data.get('membership'),
                date_pay=validated_data.get('date_pay')
            )
        
        return user
