'''
Modulo Forms
'''
from typing import Any
from django import forms

from django.forms import ModelForm
from .models import Livro, LivrosDoAutor




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

class AutorForm(forms.Form):
    '''
    Formulario Autor  
    '''
    # class Meta:
    #     '''
    #     Metamodelo
    #     '''
    #     model = LivrosDoAutor
    #     fields = ['id', 'autor', 'livro']
   