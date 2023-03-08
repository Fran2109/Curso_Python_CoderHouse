from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from InflablesApp.models import Inflable


def inicio(request):
    return render(request, 'inicio.html')

def saludo(request):
    return HttpResponse("Hola Mundo")

""" def probandoTemplate(self):
    nombre = "Francisco"
    apellido = "Filosi"
    diccionario = {"nombre": nombre, "apellido": apellido}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) """

def inflable(self):
    inflable = Inflable(nombre = "2x2", alto = 2, ancho = 2, largo = 2)
    inflable.save()
    documentoDeTexto = f"---> Inflable: {inflable.nombre}"
    return HttpResponse(documentoDeTexto)