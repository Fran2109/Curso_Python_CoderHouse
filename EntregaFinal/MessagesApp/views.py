from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from UsersApp.models import Profile

from MessagesApp.forms import FormularioMensajeNuevo
from MessagesApp.models import Mensaje


# ListaMensajes hereda de ListView y FormView, así como de LoginRequiredMixin. 
class ListaMensajes(ListView, LoginRequiredMixin, FormView):
    # Defino varias propiedades, como el modelo a usar (Mensaje), la clase de formulario a usar (FormularioMensajeNuevo), el nombre del objeto de contexto (mensajes), la URL a la que se redirige después de enviar el formulario (success_url) y la plantilla a usar (lista_mensajes.html).
    model = Mensaje
    form_class = FormularioMensajeNuevo
    context_object_name = 'mensajes'
    success_url = reverse_lazy('MessagesApp:ListaMensajes')
    template_name = 'lista_mensajes.html'
    
    # Defino el método get_queryset() que devuelve los mensajes ordenados por fecha de creación
    def get_queryset(self):
        return Mensaje.objects.order_by('fecha_creacion')
    
    # Defino el método form_valid() que guarda el formulario enviado con el autor del mensaje
    def form_valid(self, form):
        perfil = Profile.objects.filter(user=self.request.user)[0]
        form.instance.author = perfil
        form.save()
        return super().form_valid(form)

