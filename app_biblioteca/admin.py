'''
ADMIN: Registrar modelos da aplicação na área administrativa.
'''
from django.contrib import admin

# Register your models here.

from .models import (
    Autor,
    Livro,
    LivrosDoAutor,
)

admin.site.register([
    Autor,
    Livro,
    LivrosDoAutor
])
