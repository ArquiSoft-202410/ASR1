from django import forms
from .models import DatosPersonales

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['nombre', 'email', 'numero']
        labels = {'nombre': 'Nombre', 'email': 'E-Mail', 'numero': 'Numero'}