from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView

from UsersApp.forms import (FormularioEditarContrasenia,
                            FormularioEditarPerfil, FormularioLogin,
                            FormularioRegistro)
from UsersApp.models import Profile


def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            avatar = Profile(user = user, avatar = form.cleaned_data['avatar'], link = form.cleaned_data['link'])
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

class EditarPerfil(UpdateView):
    form_class = FormularioEditarPerfil
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('UsersApp:InformacionPerfil')
    def get_object(self):
        return self.request.user

class ModificarContrasenia(PasswordChangeView):
    form_class = FormularioEditarContrasenia
    template_name = 'modificar_contrasenia.html'
    success_url = reverse_lazy('MainApp:Inicio')
    
class LoginPagina(LoginView):
    form_class = FormularioLogin
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('MainApp:Inicio')

    def get_success_url(self):
        return reverse_lazy('MainApp:Inicio')