'''
Modulo Forms
'''

# from django import forms
from django.forms import EmailField, ModelForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Livro, Autor


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

# class LoginUserForm(AuthenticationForm):
#     '''
#     Login
#     '''
#     def confirm_login_allowed(self, user):
#         user = User
#         if user:
#             return user
#     class Meta:
#         '''
#         Metamodelo
#         '''
#         model = User
#         fields = ['username', 'password']


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

class PesquisarAutorForm(ModelForm):
    '''
    Pesquisar autor   
    '''
    class Meta:
        '''
        Metamodelo
        '''
        model = Autor
        fields = ['id', 'nome']

