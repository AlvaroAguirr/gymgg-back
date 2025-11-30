from django.db import models
from useraccount.models import User

# espacio para modelo ejercicios



# Create your models here.
class Routina(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rutinas',
        verbose_name="usuario dueño"
    )

    Routine_name = models.CharField(max_length=100)
    #tiemp
    Last_time_done=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.Routine_name}-{self.user.email}"
    
    # @property
    # def Total_time(self):
    #     return sum()

    # @property
    # def tiempo_total_minutos(self):
    #     return self.Total_time / 60

class RoutineHistory(models.Model):

    routine = models.ForeignKey('Routina', on_delete=models.CASCADE)
    Date_realization= models.DateTimeField(auto_now_add=True)
    #tiempo total en la que se tardo en completar en segundos
    Time_to_done= models.IntegerField()

    def __str__(self):
        return f"{self.routine.Routine_name}"

