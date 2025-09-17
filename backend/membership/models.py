import uuid
from django.db import models

class Membership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_membership = models.CharField(max_length=50)  # 'Membresía Plus'
    price_membership = models.DecimalField(max_digits=10, decimal_places=2)  # 799.00
    duration_membership = models.CharField(max_length=50,  null=True, blank=True) 
    offers_membership = models.JSONField(null=True, blank=True)  # ['Acceso...', 'Uso ilimitado...', ...]
    status_membership= models.BooleanField(default=True)

    def __str__(self):
        return self.name_membership