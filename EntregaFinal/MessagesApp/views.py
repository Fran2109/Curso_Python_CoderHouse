from django.shortcuts import render
from django.views.generic import ListView
from MessagesApp.models import Mensaje
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, FormView
from MessagesApp.forms import FormularioMensajeNuevo
from django.urls import reverse_lazy
from UsersApp.models import Profile

# Create your views here.
class ListaMensajes(ListView, LoginRequiredMixin, FormView):
    model = Mensaje
    form_class = FormularioMensajeNuevo
    context_object_name = 'mensajes'
    success_url = reverse_lazy('MessagesApp:ListaMensajes')
    template_name = 'lista_mensajes.html'
    
    def get_queryset(self):
        return Mensaje.objects.order_by('fecha_creacion')
    
    def form_valid(self, form):
        perfil = Profile.objects.filter(user=self.request.user)[0]
        form.instance.author = perfil
        form.save()
        return super().form_valid(form)

