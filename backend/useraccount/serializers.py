from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    membership = serializers.StringRelatedField()
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'

    def get_name(self, obj):
        return f"{obj.name}"
    


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
    


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = self.context['request'].user \
                   if self.context.get('request') and self.context['request'].user.is_authenticated \
                   else None
            if not user:
                user = self.authenticate(
                    self.context.get('request'),
                    email=email,
                    password=password
                )
            if not user:
                raise serializers.ValidationError('Credenciales inválidas.')
        else:
            raise serializers.ValidationError('Debe ingresar email y contraseña.')

        attrs['user'] = user
        return attrs
