from django.db import models
from django.conf import settings 

from useraccount.models import User

class ClientProfile(models.Model):
    # Relación Clave: Uno a Uno (One-to-One) con el modelo User.
    # Esto asegura que cada usuario (que no sea staff/superuser) tenga un único perfil de cliente.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, 
        related_name='client_profile',
        verbose_name="Usuario Cliente"
    )
    
    # Campos recopilados del formulario de la aplicación móvil (TrainingLevelForm)
    gender = models.CharField(max_length=50, verbose_name="Género")
    age = models.IntegerField(verbose_name="Edad")
    condition = models.CharField(max_length=100, verbose_name="Padecimiento/Condición")
    goal = models.CharField(max_length=100, verbose_name="Objetivo Fitness")
    experience = models.CharField(max_length=50, verbose_name="Nivel de Experiencia")
    duration = models.CharField(max_length=50, verbose_name="Duración del Entrenamiento Deseada")

    # Nivel de fitness calculado en el front-end
    fitness_level = models.CharField(max_length=50, default='beginner', verbose_name="Nivel de Fitness Calculado")

    class Meta:
        verbose_name = "Perfil de Cliente"
        verbose_name_plural = "Perfiles de Clientes"

    def __str__(self):
        return f"Perfil de {self.user.email}"