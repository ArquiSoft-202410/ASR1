from django import forms
from .models import DatosPersonales

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['nombres', 'apellidos', 'ciudad', 'numero', 'email']
        labels = {'nombres': 'Nombres', 'apellidos': 'Apellidos', 'numero': 'Numero', 'email': 'E-Mail'}