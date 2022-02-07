from django.db import models

# Create your models here.

#Creacion de modelo con base al los datos otorgados en el excel
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    #Nacionalidad se pone en blanco porque no se requiere debido a que se nota que hay campos en blanco en el excel
    nacionalidad = models.CharField(max_length=255, blank=True, null=True)
    fechacontrato= models.DateField()
    sexo = models.CharField(max_length=7)