from django.shortcuts import render
from InflablesApp.forms import (InflableFormulario, JuegoFormulario,
                                ReservaFormulario)
from InflablesApp.models import Inflable, Juego, Reserva


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

def busqueda(request):
    if request.method == 'GET' and 'nombre' in request.GET.keys():
        nombre = request.GET['nombre']
        if(len(nombre) > 0):
            elemento = request.GET['customRadio']
            if(elemento == 'inflable'):
                elementos = Inflable.objects.filter(nombre__icontains = nombre)
            elif(elemento == 'juego'):
                elementos = Juego.objects.filter(nombre__icontains = nombre)
            if(len(elementos) == 0):
                mensaje = f"No se han encontrado {elemento}s con el nombre: '{nombre}'"
            else:
                if(len(elementos) == 1):
                    mensaje = f"Se ha encontrado {len(elementos)} {elemento} con el nombre: '{nombre}'"
                else:
                    mensaje = f"Se han encontrado {len(elementos)} {elemento}s con el nombre: '{nombre}'"
        else:
            mensaje = "No se ha ingresado ningun nombre para buscar"
            elementos = []
    else:
        mensaje = "Selecciona que equipo quiere buscar"
        elementos = []    
    return render(request, 'busqueda.html', {"elementos": elementos, "mensaje": mensaje})

def juegos(request):
    if request.method == 'POST':
        formulario = JuegoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            juego = Juego(nombre = informacion['nombre'], cant_personas = informacion['cant_personas'], ancho = informacion['ancho'], largo = informacion['largo'])
            juego.save()
            formulario = JuegoFormulario()
    else:
        formulario = JuegoFormulario()
    
    juegos = Juego.objects.all()
    
    return render(request, 'juegos.html', {"formulario": formulario, "juegos": juegos})

def reservas(request):
    if request.method == 'POST':
        formulario = ReservaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            reserva = Reserva(fecha = informacion['fecha'], hora_inicio = informacion['hora_inicio'], hora_fin = informacion['hora_fin'], nombre_cliente = informacion['nombre_cliente'], elemento = informacion['elemento'], direccion = informacion['direccion'])
            reserva.save()
            formulario = ReservaFormulario()
    else:
        formulario = ReservaFormulario()
    
    reservas = Reserva.objects.all()
    
    return render(request, 'reservas.html', {"formulario": formulario, "reservas": reservas})