from django import forms
from MessagesApp.models import Mensaje

class FormularioMensajeNuevo(forms.ModelForm):
    contenido = forms.CharField(label=False, required=True, widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Escriba un mensaje...", 'style': "height:100px;"}))
    
    class Meta:
        model = Mensaje
        fields = ['contenido']
        help_texts = {k:"" for k in fields}