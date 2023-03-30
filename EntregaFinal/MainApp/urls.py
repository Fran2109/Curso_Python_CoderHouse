#Importo la función 'path' desde el módulo 'django.urls' y la vista 'inicio' desde 'MainApp.views'
from django.urls import path
from MainApp.views import inicio

# Defino el nombre de la aplicación como 'MainApp'
app_name = 'MainApp'

# Defino las URL para la aplicación
urlpatterns = [
    path('', inicio, name="Inicio"),
]