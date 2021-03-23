from django.shortcuts import render
from .models import Produto
from .models import Cliente

def index(request):
    qtd_produtos =Produto.objects.count()
    qtd_clientes =Cliente.objects.count()
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    context = {
        'qtd_produtos': qtd_produtos,
        'qtd_clientes': qtd_clientes,
        'produtos': produtos,
        'clientes': clientes
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos.html', context)

def clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }

    return render(request, 'clientes.html', context)

def cliente(request, pk):
    cli = Cliente.objects.get(id=pk)
    context = {
        'cliente': cli
    }
    return render(request, 'cliente.html', context)

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)