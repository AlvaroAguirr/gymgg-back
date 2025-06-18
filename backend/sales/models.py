import uuid
from django.db import models
from products.models import Product

from django.utils import timezone


class Sales(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale {self.id}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class SaleItem(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name='productos')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name_product}"

    @property
    def total_price(self):
        return self.quantity * self.unit_price
