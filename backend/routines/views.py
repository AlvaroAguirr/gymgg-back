from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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

class RoutinaViewSet(viewsets.ModelViewSet):
    serializer_class = RoutinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Routina.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RoutineHistoryViewSet(viewsets.ModelViewSet):
    queryset = RoutineHistory.objects.all()
    serializer_class = RoutineHistorySerializer
    permission_classes = [IsAuthenticated]


