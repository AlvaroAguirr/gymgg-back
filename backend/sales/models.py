import uuid
from django.db import models
from products.models import Product

class Sales(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
            return f"Sale {self.id}"
    
