#Este archivo solo se ocupara en caso de que se quiera usar el panel administrador de django
from django.contrib import admin
#Importación de librerias para el manejo de archivos
from import_export.admin import ImportExportModelAdmin
#Importación del modelo donde se estará trabajando
from .models import Persona

# Register your models here.
@admin.register(Persona)
class PersonaAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'fechacontrato', 'sexo')
