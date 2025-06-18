from django.forms import ModelForm
from .models import Membership

class PropertyForm(ModelForm):
    class Meta:
        model= Membership
        fields= {
           'name_membership',
           'price_membership',
           'offers_membership',
           'membership_duration',

        }