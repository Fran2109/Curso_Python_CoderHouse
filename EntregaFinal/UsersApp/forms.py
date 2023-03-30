from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserChangeForm, UserCreationForm)
from django.contrib.auth.models import User


# Defino una clase llamada FormularioLogin que hereda de AuthenticationForm, que es un formulario de autenticación de usuario en Django.
class FormularioLogin(AuthenticationForm):
    # Defino dos campos, uno para el nombre de usuario y otro para la contraseña, con etiquetas y widgets específicos de la clase CharField.
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    
    # Defino la clase Meta para especificar que este formulario está relacionado con el modelo de usuario y qué campos del modelo se utilizarán en este formulario.
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {k:"" for k in fields}

# Defino la clase FormularioRegistro, que hereda de UserCreationForm, que es un formulario de registro de usuario en Django.
class FormularioRegistro(UserCreationForm):
    # Defino varios campos para recopilar información del usuario, como nombre de usuario, nombre, apellido, correo electrónico, contraseña, avatar y enlace.
    username = forms.CharField(label = "Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label = "Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label = "Apellido", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    link = forms.URLField(label="Link", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    avatar = forms.ImageField(label="Ingrese su Avatar", required=True)

    # Defino la clase Meta para especificar que este formulario está relacionado con el modelo de usuario y qué campos del modelo se utilizarán en este formulario.
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'link', 'avatar']
        help_texts = {k:"" for k in fields}

# Defino una clase llamada FormularioEditarPerfil que hereda de UserChangeForm.
class FormularioEditarPerfil(UserChangeForm):
    # Defino campos de formulario utilizando la clase CharField y URLField del módulo forms de Django.
    username = forms.CharField(label = "Cambiar Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label = "Cambiar Nombre", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label = "Cambiar Apellido", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label="Cambiar Email", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = None
    link = forms.URLField(label="Cambiar Link", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    avatar = forms.ImageField(label="Ingrese su Avatar", required=False)
    
    # Defino una clase Meta dentro de la clase FormularioEditarPerfil que especifica el modelo de usuario (User) y los campos del modelo que se utilizarán en el formulario.
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'link', 'avatar']
        help_texts = {k:"" for k in fields}
    
    # Defino una función save dentro de la clase FormularioEditarPerfil que llama a la función save de la superclase UserChangeForm.
    # Luego, verifico si el formulario se ha enviado y, si es así, guardo los cambios en el objeto user.
    # Si se ha proporcionado una imagen de avatar o un enlace, actualizo el avatar o el enlace en el perfil del usuario correspondiente.
    # Finalmente, devuelvo el objeto user.
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if("avatar" in self.cleaned_data and self.cleaned_data["avatar"] is not None):
                user.profile.avatar = self.cleaned_data["avatar"]
                user.profile.save()
            if("link" in self.cleaned_data and self.cleaned_data["link"] != ""):
                user.profile.link = self.cleaned_data["link"]
                user.profile.save()
        return user

# Defino otra clase llamada FormularioEditarContrasenia que hereda de PasswordChangeForm.
class FormularioEditarContrasenia(PasswordChangeForm):
    # Defino tres campos de formulario utilizando la clase CharField del módulo forms de Django.
    old_password = forms.CharField(label=("Contraseña Actual"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nueva Contraseña"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    # Defino una clase Meta dentro de la clase FormularioEditarContrasenia que especifica el modelo de usuario (User) y los campos del modelo que se utilizarán en el formulario.
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}