from django import forms
from .models import Harvest

class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['crops']
