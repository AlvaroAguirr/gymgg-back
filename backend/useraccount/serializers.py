from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from membership.serializers import MembershipSerializer
from membership.models import Membership

from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Para mostrar datos completos al leer
    membership = MembershipSerializer(read_only=True)

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
            'password': {'write_only': True}  # No mostrar la contraseña en las respuestas
        }
 
# <<<<<<< HEAD
#     def get_name(self, obj):
#         return f"{obj.name}"
    


# class CustomRegisterSerializer(RegisterSerializer):
#     username = None  # <- Ocultamos este ca
#     name = serializers.CharField(required=True)

#     def get_cleaned_data(self):
#         print("CustomLoginSerializer.validate llamado")
#         data = super().get_cleaned_data()
#         data['name'] = self.validated_data.get('name', '')
#         data['email'] = self.validated_data.get('email', '')
#         data['password1'] = self.validated_data.get('password1', '')
#         data['password2'] = self.validated_data.get('password2', '')
#         return data
    


# class CustomLoginSerializer(LoginSerializer):
#     username = None
#     email = serializers.EmailField(required=True)

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if email and password:
#             user = self.context['request'].user \
#                    if self.context.get('request') and self.context['request'].user.is_authenticated \
#                    else None
#             if not user:
#                 user = self.authenticate(
#                     self.context.get('request'),
#                     email=email,
#                     password=password
#                 )
#             if not user:
#                 raise serializers.ValidationError('Credenciales inválidas.')
#         else:
#             raise serializers.ValidationError('Debe ingresar email y contraseña.')

#         attrs['user'] = user
#         return attrs

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

    # class Meta:
    #     model = User
    #     fields = ['id', 'name', 'email', 'password', 'membership', 'membership_id', 'date_pay', 'date_expiration']
