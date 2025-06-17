import uuid

from django.db import models
from datetime import timedelta





class Membership (models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_membership=models.CharField(max_length=50)
    price_membership=models.IntegerField()
    offers_membership=models.IntegerField(null=True)
    membership_duration=models.IntegerField() 


    def __str__(self):
        return self.name_membership
    

    
    

# Create your models here.


# tipo de membre
# precio_membe
# oferss
# duracion_mebresi