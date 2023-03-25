from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from UsersApp.models import Perfil


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
    avatar = forms.ImageField(label="Ingrese su Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'avatar']
        help_texts = {k:"" for k in fields}
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Perfil(user=user, avatar=self.cleaned_data['avatar'])
            profile.save()
        return user