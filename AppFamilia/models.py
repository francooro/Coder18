from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Persona(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField()
    profesion=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
