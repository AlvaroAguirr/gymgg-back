from django.db import models
from useraccount.models import User

# espacio para modelo ejercicios
class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Ejercicio")
    description = models.TextField(verbose_name="Descripción del Ejercicio")
    duration_seconds = models.IntegerField(verbose_name="Duración (segundos)")
    repetitions = models.IntegerField(verbose_name="Repeticiones por Serie")
    series = models.IntegerField(verbose_name="Series Recomendadas")

    # Opcional: Tipo de músculo/trabajo
    muscle_group = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Músculo o Grupo trabajados"
    )

    recommended_level = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'Principiante'),
            ('intermediate', 'Intermedio'),
            ('advanced', 'Avanzado')
        ],
        default='beginner',
        verbose_name="Nivel de Ejercicio"
    )

    Health_condition = models.CharField(
        max_length=50,
        choices=[
            ('Ninguno', 'Ninguno'),
            ('Lesión leve', 'Lesión leve'),
            ('problemas cardíacos', 'problemas cardíacos'),
            ('otro','otro')
        ],
        default='Ninguno',
        verbose_name="Condicion de salud"
    )

    # Objetivo fitness para el que está diseñado
    goal_type = models.CharField(
        max_length=100,
        choices=[
            ('Perder grasa', 'Perder Grasa'),
            ('Aumentar masa muscular', 'Aumentar masa muscular'),
            ('Resistencia', 'Resistencia'),
            ('Mantenerme', 'Mantenerme')
        ],
        verbose_name="Objetivo Compatible"
    )

    def __str__(self):
        return f"{self.name} - {self.Health_condition}-{self.muscle_group}"




class Routina(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rutinas',
        verbose_name="usuario dueño"
    )

    exercises = models.ManyToManyField(
        Exercise,
        related_name="routines",
        verbose_name="Ejercicios de la Rutina",
        blank=True
    )


    Routine_name = models.CharField(max_length=100)
    Description=models.TextField(verbose_name="descripcion", max_length=50, default="")
    Last_time_done=models.DateTimeField(null=True,blank=True)
    Times_done=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Routine_name}-{self.user.email}"
    
    @property
    def Total_time(self):
        return sum(ex.duration_seconds for ex in self.exercises.all())

    @property
    def tiempo_total_minutos(self):
        return self.Total_time / 60 if self.Total_time else 0

class RoutineHistory(models.Model):

    routine = models.ForeignKey('Routina', on_delete=models.CASCADE)
    Date_realization= models.DateTimeField(auto_now_add=True)
    #tiempo total en la que se tardo en completar en segundos
    Time_to_done= models.IntegerField()

    def __str__(self):
        return f"{self.routine.Routine_name}"

