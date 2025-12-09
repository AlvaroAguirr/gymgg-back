from rest_framework import serializers
from .models import Routina, RoutineHistory,Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class RoutineHistorySerializer(serializers.ModelSerializer):
    Routine_name = serializers.CharField(source='routine.Routine_name', read_only=True)
    Description = serializers.CharField(source='routine.Description', read_only=True)
    Last_time_done = serializers.DateTimeField(source='routine.Last_time_done', read_only=True)
    Times_done = serializers.IntegerField(source='routine.Times_done', read_only=True)
    exercises = ExerciseSerializer(source='routine.exercises', many=True, read_only=True)

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
            'total_minutes',
            'Date_realization',
            'Time_to_done'
        ]

    def get_total_time(self, obj):
        return obj.routine.Total_time if obj.routine else 0

    def get_total_minutes(self, obj):
        return obj.routine.tiempo_total_minutos if obj.routine else 0


class RoutinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routina
        fields = "__all__"