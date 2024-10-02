'''
VIEWS
'''
from datetime import datetime
from django.http import Http404
from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    redirect
)
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Autor, LivrosDoAutor, Livro
from .forms import PesquisarLivroForm, RegistrationForm, PesquisarAutorForm


def sign_up(request):
    '''
    sign_up
    '''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_edit(request, user_id: int) -> HttpResponse:
    '''
    Editar usuário
    '''
   
    try:
        um_usuario = User.objects.get(pk=user_id)
    except User.DoesNotExist as not_found:
        raise Http404(
            f"Usuário não encontrado! O Usuário de ID={user_id} não existe na base de dados."
        ) from not_found

    contexto = {
        'usuario': um_usuario
    }
    return render(request, 'user_edit.html', context=contexto)



def user_save(request, user_id: int) -> HttpResponse:
    '''
    Salvar edição de usuário
    '''
    try:
        if user_id == 0:
            um_usuario = User.objects.create(criado_em=datetime.now())
        else:
            um_usuario = User.objects.get(pk=user_id)
    except User.DoesNotExist as not_found:
        raise Http404(
            f"Usuário não encontrado! O Usuário de ID={user_id} não existe na base de dados."
        ) from not_found
    
    um_usuario.username = request.POST["username"]
    um_usuario.email = request.POST["email"]

    um_usuario.save()
    return HttpResponseRedirect(reverse("home"))

def password_edit(request, user_id: int) -> HttpResponse:
    '''
    Editar senha
    '''
   
    try:
        um_usuario = User.objects.get(pk=user_id)
    except User.DoesNotExist as not_found:
        raise Http404(
            f"Usuário não encontrado! O Usuário de ID={user_id} não existe na base de dados."
        ) from not_found

    contexto = {
        'usuario': um_usuario
    }
    return render(request, 'password_edit.html', context=contexto)



def home(request) -> HttpResponse:
    '''
    Home
    '''
    return render(request, 'home.html')

def autor(request, autor_id: int) -> HttpResponse:
    '''
    Autor
    '''
    try:
        um_autor = Autor.objects.get(pk=autor_id)
    except Autor.DoesNotExist as not_found:
        print(not_found)
        raise Http404(
            f"Autor não encontrado! O autor de ID={autor_id} não existe na base de dados."
        ) from not_found
    livros_autor = LivrosDoAutor.objects.filter(autor_id=autor_id)
    contexto = {
        'autor': um_autor,
        'livros': livros_autor
    }
    return render(request, 'autor.html', context=contexto)

def autor_delete(request, autor_id: int) -> HttpResponse:
    '''
    Autor
    '''
    try:
        um_autor = Autor.objects.get(pk=autor_id)
        um_autor.delete()
    except Autor.DoesNotExist as not_found:
        print(not_found)
        raise Http404(
            f"Autor não encontrado! O autor de ID={autor_id} não existe na base de dados."
        ) from not_found

    return HttpResponseRedirect(reverse("autores"))

def autor_add(request) -> HttpResponse:
    '''
    Autor
    '''
    contexto = {
        'autor': Autor.objects.create(criado_em=datetime.now())
    }
    return render(request, 'autor_edit.html', context=contexto)

def autor_edit(request, autor_id: int) -> HttpResponse:
    '''
    Autor
    '''
    try:
        um_autor = Autor.objects.get(pk=autor_id)
    except Autor.DoesNotExist as not_found:
        print(not_found)
        raise Http404(
            f"Autor não encontrado! O autor de ID={autor_id} não existe na base de dados."
        ) from not_found

    contexto = {
        'autor': um_autor
    }
    return render(request, 'autor_edit.html', context=contexto)


def autor_save(request, autor_id: int) -> HttpResponse:
    '''
    Autor
    '''
    try:
        if autor_id == 0:
            um_autor = Autor.objects.create(criado_em=datetime.now())
        else:
            um_autor = Autor.objects.get(pk=autor_id)
    except Autor.DoesNotExist as not_found:
        print(not_found)
        raise Http404(
            f"Autor não encontrado! O autor de ID={autor_id} não existe na base de dados."
        ) from not_found

    um_autor.nome = request.POST["nome"]
    # um_autor.criado_em = request.POST["criado_em"]
    # um_autor.criado_em = request.POST["criado_em"]
    um_autor.save()
    return HttpResponseRedirect(reverse("autor", args=(autor_id,)))

def autores(request) -> HttpResponse:
    '''
    Autores
    '''
    if request.method == "POST":
        nome = request.POST['nome']
        um_autor = Autor.objects.filter(nome__icontains=nome).first()
        if um_autor:
            return HttpResponseRedirect(reverse("autor", args=(um_autor.id,)))
        raise Http404(f"Autor de nome {nome} não encontrado!")

    lista = Autor.objects.order_by('nome')
    form = PesquisarAutorForm()
    return render(request, 'autores.html', {
        "form": form,
        "autores": lista,
    })

def livros(request) -> HttpResponse:
    '''
   livros
    '''
    if request.method == "POST":
        titulo = request.POST['titulo']
        um_livro = Livro.objects.filter(titulo__icontains=titulo).first()
        if um_livro:
            return HttpResponseRedirect(reverse("livro", args=(um_livro.id,)))
        raise Http404(f"O livro de título {titulo} não encontrado!")

    lista = Livro.objects.all()
    form = PesquisarLivroForm()
    return render(request, 'livros.html', {
        "form": form,
        "livros": lista,
    })


def livro(request, livro_id: int) -> HttpResponse:
    '''
    livro
    '''
    try:
        um_livro = Livro.objects.get(pk=livro_id)
    except Livro.DoesNotExist as not_found:
        raise Http404(
            f"Livro não encontrado! O Livro de ID={livro_id} não existe na base de dados."
        ) from not_found
   
    livros_autor = LivrosDoAutor.objects.filter(livro_id=livro_id)
    contexto = {
        'livro': um_livro,
        'autores': livros_autor
    }

    return render(request, 'livro.html', context=contexto)

