'''
MODELS da aplicação Biblioteca
'''
from django.db import models
# from django.contrib.auth.models import AbstractUser

class Autor(models.Model):
    '''
    Autor
    '''
    nome = models.CharField('Nome do Autor', max_length=30)
    criado_em = models.DateTimeField('criado')
    informacaoes = models.TextField('Informações', default='')
    fonte_informacao = models.CharField('Fonte', max_length=100, default='')

   

    def __str__(self):
        '''
        str
        '''
        return str(self.nome)
   
    class Meta:
        '''
        Meta Autor
        '''
        db_table = 'autor'

class Livro(models.Model):
    '''
    Livro
    '''
    titulo = models.CharField('Título', max_length=300)
    criado_em = models.DateField('criado', help_text='yyyy/mm/dd')
    ano = models.IntegerField('ano da publicação', default=2024)
    informacaoes = models.TextField('Informações', default='')
    fonte_informacao = models.CharField('Fonte', max_length=100, default='')

    def __str__(self):
        '''
        str
        '''
        return str(self.titulo)

    class Meta:
        '''
        Meta Livro
        '''
        db_table = 'livro'

class LivrosDoAutor(models.Model):
    '''
    Livros do Autor
    '''
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Livro {self.livro} | autor {self.autor}"
    
    class Meta:
        '''
        Meta LivrosDoAutor
        '''
        db_table = 'livros_do_autor'


# class CustomUser(AbstractUser):
#     bio = models.CharField(max_length=128, null=True, blank=True)