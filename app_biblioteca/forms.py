'''
Modulo Forms
'''

# from django import forms
from django.forms import EmailField, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
from .models import Livro


class RegistrationForm(UserCreationForm):
    '''
    Registra Usuário
    '''
    email = EmailField(required=True)
    class Meta:
        '''
        Metamodelo
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PesquisarLivroForm(ModelForm):
    '''
    Pesquisar livro    
    '''
    class Meta:
        '''
        Metamodelo
        '''
        model = Livro
        fields = ['id', 'titulo']
