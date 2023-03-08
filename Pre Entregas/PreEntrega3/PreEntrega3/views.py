from django.http import HttpResponse
from django.template import Context, Template, loader

def saludo(request):
    return HttpResponse("Hola Mundo")

def probandoTemplate(self):
    nombre = "Francisco"
    apellido = "Filosi"
    diccionario = {"nombre": nombre, "apellido": apellido}
    # miHtml = open("C:/Users/Francisco/Desktop/Curso_Python_CoderHouse/Pre Entregas/PreEntrega3/PreEntrega3/templates/template1.html")
    # plantilla = Template(miHtml.read())
    # miHtml.close()
    # miContexto = Context(diccionario)
    # documento = plantilla.render(miContexto)
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)