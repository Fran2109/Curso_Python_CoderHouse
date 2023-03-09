from django.urls import path
from InflablesApp.views import *

app_name = "InflablesApp"

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inflables/', inflables, name="Inflables"),
    path('eliminarInflable/<inflableId>/', eliminarInflable, name="EliminarInflable"),
    path('juegos/', juegos, name="Juegos"),
    path('busqueda/', busqueda, name="Busqueda")
]
