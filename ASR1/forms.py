from django import forms
from .models import DatosPersonales

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['nombres', 'apellidos', 'pais', 'ciudad', 'numero', 'email']
        labels = {'nombres': 'Nombres', 'apellidos': 'Apellidos', 'pais': 'Pais', 'numero': 'Numero', 'email': 'E-Mail'}