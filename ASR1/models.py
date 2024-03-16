from django.db import models

class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.CharField(max_length=12)