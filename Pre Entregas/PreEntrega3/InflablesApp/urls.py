from django.urls import path
from InflablesApp.views import *

app_name = "InflablesApp"

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inflables/', inflables, name="Inflables"),
]
