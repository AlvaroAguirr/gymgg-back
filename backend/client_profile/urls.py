from django.urls import path
from . import views

urlpatterns = [
    # 1. Ruta para OBTENER el perfil de fitness (Método HTTP: GET)
    path('get/', views.get_client_profile, name='get_client_profile'),
    # 2. Ruta para GUARDAR o ACTUALIZAR el perfil de fitness (Método HTTP: POST)
    path('save/', views.save_client_profile, name='save_client_profile'),
]