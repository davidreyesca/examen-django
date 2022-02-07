from django.shortcuts import render
from .models import Persona
from django.contrib import messages
from tablib import Dataset
from django.db.models import Count
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        dataset = Dataset()
        nueva_persona = request.FILES['myfile']

        if not nueva_persona.name.endswith('xlsx'):
            messages.error(request, 'Formato de archivo no valido')
            return render(request, 'index.html')

        imported_data = dataset.load(nueva_persona.read(), format='xlsx')

        for data in imported_data:
            value = Persona(
                nombre=data[0],
                apellido=data[1],
                nacionalidad=data[2],
                fechacontrato=data[3],
                sexo=data[4])
            value.save()
        messages.error(request, 'Archivos cargado con exito!, Pulsa el botón de "Ver todos los datos" para continuar')
        return render(request, 'index.html')
    return render(request, 'index.html')

#Creación del controlador para mostrar todos los datos
def datos(request):
    persona = Persona.objects.all()
    return render(request, 'datos.html', {"query": persona})

#Creación del controlador para graficar el sexo
def graficarSexo(request):
    #Obtención de datos unicamente de la columna sexo, usando un group by para poderlo graficar
    sexo = Persona.objects.values('sexo').annotate(dcount=Count('sexo')).order_by()
    sexoJson = json.dumps(list(sexo)) # convert to JSON
    return render(request, 'graficasSexo.html', {"sexo": sexoJson})

#Creación del controlador para graficar el nacionalidad
def graficarNacionalidad(request):
    #Obtención de datos unicamente de la columna nacionalidad, usando un group by para poderlo graficar
    nacionalidad = (Persona.objects.values('nacionalidad').annotate(dcount=Count('nacionalidad')).order_by())
    nacionalidadJson = json.dumps(list(nacionalidad)) # convert to JSON
    return render(request, 'graficasNacionalidad.html', {"nacionalidad": nacionalidadJson})