from django.contrib.auth.forms import UserCreationForm #criacao de conta
from .models import Usuario
from django import forms


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField() #criando o campo email
    
    class Meta: #necessario para o UserCreationForm
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2') #campos q irao mostrar na criacao de conta
        