from django.forms import ModelForm
from .models import Product

class PropertyForm(ModelForm):
    class Meta:
        model = Product
        fields = {
            'id',
            'name_product',
            'price_product',
            'description',
            'stock',
            'category',
        }