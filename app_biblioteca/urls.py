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
    path("livros/", views.livros, name='livros'),
    path("livro/<int:livro_id>", views.livro, name='livro'),
    path("register/", views.sign_up, name='sign_up'),
    path("user_edit/<int:user_id>", views.user_edit, name='user_edit'),
    path("password_edit/<int:user_id>", views.password_edit, name='password_edit'),
    path("user_save/<int:user_id>", views.user_save, name='user_save'),

]
