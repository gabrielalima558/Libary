from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# cuidado com o import as vezes se deixar o caminho completo da erro, aparece no log
from .models import Livro


# Create your views here.


def index(request):
    dados = {
        'livros': Livro.objects.all()
    }
    # envio as infos de livros para o meu template através do render
    return render(request, 'index.html', dados)


def livro(request, id):
    livro = {
        'livro': get_object_or_404(Livro, pk=id)
    }
    return render(request, 'livro.html', livro)


def emprestimo(request):
    dados = {
        'livros': Livro.objects.filter(emprestado=False)
    }
    return render(request, 'index.html', dados)
