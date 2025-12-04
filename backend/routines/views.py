from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Routina, RoutineHistory
from .serializers import RoutinaSerializer, RoutineHistorySerializer

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
