from django.urls import path
from InflablesApp.views import *

app_name = "InflablesApp"

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inflables/', leerInflables, name="Inflables"),
    path('eliminarInflable/<inflableId>/', eliminarInflable, name="EliminarInflable"),
    path('editarInflable/<inflableId>/', editarInflable, name="EditarInflable"),
    path('juegos/', juegos, name="Juegos"),
    path('busqueda/', busqueda, name="Busqueda"),
    path('reservas/', reservas, name="Reservas"),
]
