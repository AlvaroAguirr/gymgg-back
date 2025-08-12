from rest_framework import serializers

from membership.models import Membership

from .models import User


class UserSerializer(serializers.ModelSerializer):
    membership = serializers.PrimaryKeyRelatedField(queryset=Membership.objects.all())
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # no devolver la password
        }

    def get_name(self, obj):
        return f"{obj.name}"
    


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # importante para hash
        user.save()
        return user