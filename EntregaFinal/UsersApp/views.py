from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from UsersApp.forms import FormularioLogin, FormularioRegistro
from UsersApp.models import Profile


# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = FormularioLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("MainApp:Inicio")
            else:
                return render(request, 'login.html', {"form": form})
        else:
            return render(request, 'login.html', {"form": form})
    form = FormularioLogin()
    return render(request, 'login.html', {"form": form})
  
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if 'avatar' in request.FILES:
                avatar = Profile(user = user, avatar = form.cleaned_data['avatar'])
                avatar.save()
            return redirect("MainApp:Inicio")
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {"form": form})

def acercaDeMi(request):
    context = {
        'nombre': 'Francisco',
        'apellido': 'Filosi',
        'profesion': 'Desarrollador RPA',
        'nacionalidad': 'Argentino',
        'ciudad': 'Tortuguitas',
        'edad': 21,
        'email': 'franciscofilosi3@gmail.com',
        'telefono': '11-5591-1624',
        'descripcion': 'Soy desarrollador RPA en Automation Anywhere hace un año. Estoy apuntando a especializarme en IA y estoy estudiando Ingenieria en Informatica en la UCEMA. Actualmente estoy cursando el tercer año de la carrera.'
    }
    return render(request, 'acerca_de_mi.html', context)

@login_required
def informacionPerfil(request):
    return render(request, 'informacion_perfil.html', {})