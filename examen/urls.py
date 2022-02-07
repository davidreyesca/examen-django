"""examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Se importan las views de la aplicación que queremos
from upload_excel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Se añade la ruta para la vista de la aplicación - upload_excel cargará en cuanto se corra el proyecto
    path('', views.index),
    path('datos/', views.datos),
    path('graficarNacionalidad/', views.graficarNacionalidad),
    path('graficarSexo/', views.graficarSexo),
]
