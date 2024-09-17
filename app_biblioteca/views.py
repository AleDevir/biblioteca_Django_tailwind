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
from .models import Autor, LivrosDoAutor

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
    lista = Autor.objects.order_by('nome')
    contexto = {
        'autores': lista
    }
    return render(request, 'autores.html', context=contexto)
