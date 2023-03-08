from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from InflablesApp.models import Inflable


def inicio(request):
    return render(request, 'inicio.html')

def inflables(request):
    return render(request, 'inflables.html')


""" def probandoTemplate(self):
    nombre = "Francisco"
    apellido = "Filosi"
    diccionario = {"nombre": nombre, "apellido": apellido}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) """

