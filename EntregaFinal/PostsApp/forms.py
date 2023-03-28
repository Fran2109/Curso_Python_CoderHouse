from django import forms
from PostsApp.models import Post


class FormularioNuevoPost(forms.ModelForm):
    titulo = forms.CharField(label = "Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    subtitulo = forms.CharField(label = "Sub-Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    contenido = forms.CharField(label = "Contenido del Post", required=True, widget=forms.Textarea(attrs={'class': "form-control"}))
    fondo = forms.ImageField(label="Fondo del Post", required=True)
    
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'fondo']
        help_texts = {k:"" for k in fields}
        
class FormularioEdicionPost(forms.ModelForm):
    titulo = forms.CharField(label = "Nuevo Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    subtitulo = forms.CharField(label = "Nuevo Sub-Titulo del Post", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    contenido = forms.CharField(label = "Nuevo Contenido del Post", required=True, widget=forms.Textarea(attrs={'class': "form-control"}))
    fondo = forms.ImageField(label="Nuevo Fondo del Post", required=True)
    
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'fondo']
        help_texts = {k:"" for k in fields}