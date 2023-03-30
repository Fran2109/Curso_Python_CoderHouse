# Importo varios módulos y clases de Django.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
# Importo los formularios y modelos personalizados de mi aplicación.
from UsersApp.forms import (FormularioEditarContrasenia,
                            FormularioEditarPerfil, FormularioLogin,
                            FormularioRegistro)
from UsersApp.models import Profile


# Defino una vista de función que renderiza información personal sobre mí en una plantilla
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
        'descripcion': 'Soy desarrollador RPA en Automation Anywhere hace un año.Estoy apuntando a especializarme en IA y estoy estudiando Ingenieria en Informatica en la UCEMA. Actualmente estoy cursando el tercer año de la carrera.'
    }
    return render(request, 'acerca_de_mi.html', context)

# Defino una vista de función que renderiza la información del perfil del usuario logueado en una plantilla si está autenticado, de lo contrario lo redirige a la página de inicio de sesión
@login_required
def informacionPerfil(request):
    return render(request, 'informacion_perfil.html', {})

# Defino una clase FormView personalizada para el registro de usuario en la que se maneja la creación del objeto de perfil del usuario y el inicio de sesión del usuario después de registrarse con éxito
class Registro(FormView):
    model = Profile
    template_name = 'registro.html'
    form_class = FormularioRegistro
    redirect_autheticated_user = True
    success_url = reverse_lazy('MainApp:Inicio')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            avatar = Profile(user = user, avatar = form.cleaned_data['avatar'], link = form.cleaned_data['link'])
            avatar.save()
        return super(Registro, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('MainApp:Inicio')
        return super(Registro, self).get(*args, **kwargs)

# Defino una clase UpdateView personalizada para que el usuario pueda editar su perfil si está autenticado.
# El perfil que se actualiza es el del usuario actual 
class EditarPerfil(LoginRequiredMixin, UpdateView):
    form_class = FormularioEditarPerfil
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('UsersApp:InformacionPerfil')
    def get_object(self):
        return self.request.user
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super(EditarPerfil, self).get(*args, **kwargs)
        return redirect('UsersApp:Login')

# Defino una clase PasswordChangeView personalizada para permitir que el usuario cambie su contraseña si está autenticado
class ModificarContrasenia(PasswordChangeView):
    form_class = FormularioEditarContrasenia
    template_name = 'modificar_contrasenia.html'
    success_url = reverse_lazy('MainApp:Inicio')

# Defino una clase LoginView personalizada para permitir que el usuario se logue si esta registrado
class Login(LoginView):
    form_class = FormularioLogin
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('MainApp:Inicio')

    def get_success_url(self):
        return reverse_lazy('MainApp:Inicio')