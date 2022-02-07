#Se creará un archivo resource.py donde estará toda la lógica de la librería.
from cmath import rect
from import_export import resources
from .models import Persona


class PersonaResource(resources.ModelResource):
    class meta:
        #Defino que toda la información del modelo se exportará sin exclusión de campos
        model = Persona