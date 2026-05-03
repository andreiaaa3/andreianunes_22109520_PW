from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Artigo, Like
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/artigos.html', {'artigos': artigos})


def artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)
    comentarios = artigo.comentarios.all()
    form = ComentarioForm()

    return render(request, 'artigos/artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form,
    })


@login_required
def novo_artigo_view(request):
    if not is_autor(request.user):
        return redirect('artigos')

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')

    return render(request, 'artigos/novo_artigo.html', {'form': form})


@login_required
def edita_artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)

    if artigo.autor != request.user:
        return redirect('artigos')

    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)

    if form.is_valid():
        form.save()
        return redirect('artigo', id=artigo.id)

    return render(request, 'artigos/edita_artigo.html', {
        'form': form,
        'artigo': artigo,
    })


def like_artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)
    Like.objects.create(artigo=artigo)
    return redirect('artigo', id=artigo.id)


@login_required
def comentario_artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)

    form = ComentarioForm(request.POST or None)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.autor = request.user
        comentario.save()

    return redirect('artigo', id=artigo.id)