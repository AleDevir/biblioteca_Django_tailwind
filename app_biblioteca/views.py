'''
VIEWS
'''
from datetime import datetime
from django.http import Http404
from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
)
from django.urls import reverse
from .models import Autor, LivrosDoAutor, Livro
from .forms import PesquisarLivroForm

def home(request) -> HttpResponse:
    '''
    Home
    '''
    return render(request, 'home.html')

def erro500(request) -> HttpResponse:
    '''
    erro 500
    '''
    return 1/0

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
    lista = Autor.objects.order_by('nome')
    contexto = {
        'autores': lista
    }
    return render(request, 'autores.html', context=contexto)

def livros(request) -> HttpResponse:
    '''
   livros
    '''
    if request.method == "POST":
        titulo = request.POST['titulo']
        lista = Livro.objects.filter(titulo__icontains=titulo)
        if lista:
            return HttpResponseRedirect(reverse("livro", args=(lista[0].id,)))
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
        print(f"not_found 404 {not_found}")
        raise Http404(
            f"Livro não encontrado! O Livro de ID={livro_id} não existe na base de dados."
        ) from not_found
   
    livros_autor = LivrosDoAutor.objects.filter(livro_id=livro_id)
    contexto = {
        'livro': um_livro,
        'autores': livros_autor
    }

    return render(request, 'livro.html', context=contexto)
