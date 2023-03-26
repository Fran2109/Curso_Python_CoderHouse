from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from UsersApp.models import Profile


class FormularioLogin(AuthenticationForm):
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {k:"" for k in fields}
    
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label = "Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label = "Apellido", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    link = forms.URLField(label="Link", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    avatar = forms.ImageField(label="Ingrese su Avatar", required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'link', 'avatar']
        help_texts = {k:"" for k in fields}
        
class FormularioEditarPerfil(UserCreationForm):
    username = forms.CharField(label = "Cambiar Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label = "Cambiar Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label = "Cambiar Apellido", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Cambiar Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    link = forms.URLField(label="Cambiar Link", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    avatar = forms.ImageField(label="Ingrese su Avatar", required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'link', 'avatar']
        help_texts = {k:"" for k in fields}