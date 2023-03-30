from django import forms
from PostsApp.models import Post


# Defino la clase 'FormularioNuevoPost' que hereda de 'forms.ModelForm'.
class FormularioNuevoPost(forms.ModelForm):
    # Defino los campos que contendrá el formulario y las características de cada uno, como etiquetas, requerimientos, y widgets.
    titulo = forms.CharField(label = "Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    subtitulo = forms.CharField(label = "Sub-Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    contenido = forms.CharField(label = "Contenido del Post", required=True, widget=forms.Textarea(attrs={'class': "form-control"}))
    fondo = forms.ImageField(label="Fondo del Post", required=True)
    
    # La clase Meta del formulario define el modelo que se utilizará para crear el formulario y los campos del modelo que se utilizarán en el formulario.
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'fondo']
        help_texts = {k:"" for k in fields}

# La clase FormularioEdicionPost es igual a a clase FormularioNuevoPost cambiando el label de los inputs para resaltar la edicion
class FormularioEdicionPost(forms.ModelForm):
    titulo = forms.CharField(label = "Nuevo Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    subtitulo = forms.CharField(label = "Nuevo Sub-Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    contenido = forms.CharField(label = "Nuevo Contenido del Post", required=True, widget=forms.Textarea(attrs={'class': "form-control"}))
    fondo = forms.ImageField(label="Nuevo Fondo del Post", required=True)
    
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'fondo']
        help_texts = {k:"" for k in fields}