from rest_framework import serializers
from .models import Routina, RoutineHistory

class RoutineHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineHistory
        fields = "__all__"


class RoutinaSerializer(serializers.ModelSerializer):
    historial = RoutineHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Routina
        fields = "__all__"