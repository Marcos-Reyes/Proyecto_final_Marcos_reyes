from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    numero= forms.IntegerField(required=True)
    Stock = (
        ("Hay Stock (consultar cantidad)","Hay Stock (consultar cantidad)"),
        ("Sin Stock","Sin stock"),
        )
    stock = forms.ChoiceField(label="stock", choices=Stock, required=True)

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    apellido= forms.CharField(max_length=50, required=True)
    email= forms.EmailField(required=True)

class ProveedorForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    apellido= forms.CharField(max_length=50, required=True)
    email= forms.EmailField(required=True)

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
  
