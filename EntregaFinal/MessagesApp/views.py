from django.shortcuts import render
from django.views.generic import ListView
from MessagesApp.models import Mensaje
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ListaMensajes(ListView, LoginRequiredMixin):
    model = Mensaje
    context_object_name = 'mensajes'
    template_name = 'lista_mensajes.html'
    
    def get_queryset(self):
        return Mensaje.objects.order_by('fecha_creacion')