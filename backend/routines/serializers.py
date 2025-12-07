from rest_framework import serializers
from .models import Routina, RoutineHistory,Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class RoutineHistorySerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    total_time = serializers.SerializerMethodField()
    total_minutes = serializers.SerializerMethodField()

    class Meta:
        model = RoutineHistory
        fields = [
            'id',
            'Routine_name',
            'Description',
            'Last_time_done',
            'Times_done',
            'exercises',
            'total_time',      
            'total_minutes'     
        ]

    def get_total_time(self, obj):
        return obj.Total_time

    def get_total_minutes(self, obj):
        return obj.tiempo_total_minutos


class RoutinaSerializer(serializers.ModelSerializer):
    historial = RoutineHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Routina
        fields = "__all__"
