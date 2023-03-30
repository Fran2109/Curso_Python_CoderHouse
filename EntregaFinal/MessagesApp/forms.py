# Importo el módulo 'forms' de Django y el modelo 'Mensaje' desde el módulo 'MessagesApp.models'
from django import forms
from MessagesApp.models import Mensaje

# Defino un formulario para crear un nuevo mensaje que hereda de 'ModelForm'.
class FormularioMensajeNuevo(forms.ModelForm):
    # Defino el campo 'contenido' como un campo de texto que utiliza el widget 'Textarea' de Django. 
    # También uso una etiqueta, un marcador de posición y un estilo para el widget.
    contenido = forms.CharField(label=False, required=True, widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Escriba un mensaje...", 'style': "height:100px;"}))
    
    # El modelo que se utilizará para generar el formulario, así como los campos que se mostrarán en el formulario. Además, se define un diccionario de ayuda vacío que se utiliza para eliminar cualquier texto de ayuda predeterminado generado por Django.
    class Meta:
        model = Mensaje
        fields = ['contenido']
        help_texts = {k:"" for k in fields}