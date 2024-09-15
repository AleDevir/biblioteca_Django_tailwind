'''
URLs Aplicação Biblioteca
'''

from django.urls import path

from . import views

APP_NAME = 'app_biblioteca'

urlpatterns = [
    path("", views.home, name='home'),
    path("autor_add", views.autor_add, name='autor_add'),
    path("autor/<int:autor_id>", views.autor, name='autor'),
    path("autor_edit/<int:autor_id>", views.autor_edit, name='autor_edit'),
    path("autor_save/<int:autor_id>", views.autor_save, name='autor_save'),
    path("autor_delete/<int:autor_id>", views.autor_delete, name='autor_delete'),
    path("autores/", views.autores, name='autores'),
]
