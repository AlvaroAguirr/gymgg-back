from rest_framework import serializers

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