from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    membership = serializers.StringRelatedField()
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'

    def get_name(self, obj):
        return f"{obj.name}"