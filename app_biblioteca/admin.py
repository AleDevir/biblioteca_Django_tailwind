'''
ADMIN: Registrar modelos da aplicação na área administrativa.
'''

from django.contrib import admin


from .models import (
    Autor,
    Livro,
    LivrosDoAutor,
)

admin.site.register([
    Autor,
    Livro,
    LivrosDoAutor,

])

