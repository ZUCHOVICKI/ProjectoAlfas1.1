from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario",max_length=50,min_length=5,required=True,
    widget=forms.TextInput(attrs={'placeholder':'Ingresa Tu usuario','class':'form-control'}))
    password = forms.CharField(label="Contraseña",max_length=50,min_length=5,required=True,
    widget=forms.PasswordInput(attrs={'placeholder':'Ingresa Tu contraseña','class':'form-control'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        widgets = {
        'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa Tu Username'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingresa una Contraseña'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingresa Tu Email'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu Nombre'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu Apellido'}),

        }
        help_texts = {
        'username':'Maximo 50 Caracteres',
        'password':'Maximo 8 Caracteres'

        }
