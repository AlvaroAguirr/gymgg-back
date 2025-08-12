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
        source='membership',  # Asigna al campo real
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'membership', 'membership_id', 'date_pay', 'date_expiration']