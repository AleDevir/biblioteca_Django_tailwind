'''
MODELS da aplicação Biblioteca
'''
from django.db import models

# Create your models here.

class Autor(models.Model):
    '''
    Autor
    '''
    nome = models.CharField('Nome do Autor', max_length=30)
    criado_em = models.DateTimeField('criado')

    def __str__(self):
        '''
        str
        '''
        return str(self.nome)


class Livro(models.Model):
    '''
    Livro
    '''
    titulo = models.CharField('Título do Livro', max_length=30)
    criado_em = models.DateTimeField('criado')

    def __str__(self):
        '''
        str
        '''
        return str(self.titulo)


class LivrosDoAutor(models.Model):
    '''
    Livros do Autor
    '''
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Livro {self.livro} do autor {self.autor}"
