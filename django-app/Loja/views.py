from django.shortcuts import render, redirect

# Create your views here.
from .models import Products

def index(request):
    produtos = Products.objects.all()
    return render(request, 'pages/index.html', {'produtos': produtos})

def busca(request):
    pesquisa = request.GET.get('busca')
    produtos = Products.objects.filter(name__icontains=pesquisa)
    return render(request, 'pages/index.html', {'produtos': produtos})

def adicionar(request):
    nome = request.POST.get('nome')
    preco = request.POST.get('preco')
    imagem = request.FILES.get('imagem')
    descricao = request.POST.get('descricao')

    Products.objects.create(name=nome, price=preco, image=imagem, description = descricao)

    return redirect('home')