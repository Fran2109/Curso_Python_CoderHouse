from django.shortcuts import render
from InflablesApp.forms import InflableFormulario
from InflablesApp.models import Inflable


def inicio(request):
    return render(request, 'inicio.html')

def inflables(request):
    if request.method == 'POST':
        formulario = InflableFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            inflable = Inflable(nombre = informacion['nombre'], alto = informacion['alto'], ancho = informacion['ancho'], largo = informacion['largo'])
            inflable.save()
            formulario = InflableFormulario()
    else:
        formulario = InflableFormulario()
    
    inflables = Inflable.objects.all()
    
    return render(request, 'inflables.html', {"formulario": formulario, "inflables": inflables})

def eliminarInflable(request, inflableId):
    inflable = Inflable.objects.get(id = inflableId)
    inflable.delete()
    inflables = Inflable.objects.all()
    return render(request, 'inflables.html', {"formulario": InflableFormulario(), "inflables": inflables})

