from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from datetime import datetime
from django.utils.dateparse import parse_datetime

import math 
import calendar 

from .models import Routina, RoutineHistory,Exercise
from .serializers import RoutinaSerializer, RoutineHistorySerializer,ExerciseSerializer


#funcion para filtar ejercicios segun info de usuario
def recommend_exercises_for_user(user):
    profile = user.client_profile


    print("Nivel:", profile.fitness_level)
    print("Objetivo:", profile.goal)

    exercises = Exercise.objects.filter(
        recommended_level=profile.fitness_level,
        goal_type=profile.goal
    )

    print("Ejercicios encontrados:", exercises.count())

    return exercises

# viewset para SOLO leer ejercicios segun el filtro
class ExcerciseRecommendationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExerciseSerializer


    def list(self, request, *args, **kwargs):
        print("Entré a LIST (recomendaciones)")
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        print("Entré a GET_QUERYSET (recomendaciones)")
        return recommend_exercises_for_user(self.request.user)
    



#ViewSet obtener la lista de todos los ejercisos
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def by_ids(self, request):
        """
        POST /exercises/by_ids/
        Body: { "ids": [1,2,5] }
        """
        ids = request.data.get("ids", None)

        if not ids or not isinstance(ids, list):
            return Response(
                {"error": "Se requiere una lista de IDs."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        exercises = Exercise.objects.filter(id__in=ids)
        serializer = self.get_serializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoutinaViewSet(viewsets.ModelViewSet):
    serializer_class = RoutinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Routina.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#filtrado para historial

class RoutineHistoryViewSet(viewsets.ModelViewSet):
    queryset = RoutineHistory.objects.all()
    serializer_class = RoutineHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return RoutineHistory.objects.filter(routine__user=user)

    # Filtrado por mes
    @action(detail=False, methods=['get'])
    def all_months(self, request):
        hoy=timezone.now()
        year= hoy.year
        queryset= self.get_queryset().filter(
            Date_realization__year=year
        ).order_by("Date_realization")

        serializer = self.get_serializer(queryset, many=True)
        data=serializer.data
        
        result= {}

        # Crear estructura base para los 12 meses
        for month in range(1, 13):
            month_name = calendar.month_name[month]

            result[month_name] = {
                "week_1": [],
                "week_2": [],
                "week_3": [],
                "week_4": [],
                "week_5": [],
            }
        for item in data:
            fecha = parse_datetime(item["Date_realization"]).date()
            day=fecha.day

            week_number = math.ceil(day / 7)
            week_key = f"week_{week_number}"

            month_name = calendar.month_name[fecha.month]
            result[month_name][week_key].append(item)

        return Response(result)


   # Filtrar por semana
    @action(detail=False, methods=['get'])
    def this_week(self, request):
        hoy = timezone.now()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + timedelta(days=6)
        queryset = self.get_queryset().filter(
            Date_realization__date__range=[inicio_semana.date(), fin_semana.date()]
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

