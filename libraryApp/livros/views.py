from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro


def index(request):
    dados = {
        'livros': Livro.objects.all()
    }
    return render(request, 'index.html', dados)


def livro(request, livro_id):
    livro = {
        'livro': get_object_or_404(Livro, pk=livro_id)
    }
    return render(request, 'livro.html', livro)


def emprestimo(request):
    if not request.user.is_authenticated:
        return redirect('index')

    dados = {
        'livros': Livro.objects.filter(emprestado=False)
    }
    return render(request, 'index.html', dados)


def busca(request):
    livros = Livro.objects.order_by('titulo').all()

    if 'titulo' in request.GET:
        titulo = request.GET['titulo']
        if titulo:
            livros = livros.filter(titulo__icontains=titulo)

    dados = {
        'livros': livros
    }

    return render(request, 'index.html', dados)