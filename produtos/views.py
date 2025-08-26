from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

def cadastrar_produto(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome_do_produto')
        preco = request.POST.get('preco_do_produto')
        
        produto = Produto(nome=nome, preco=preco)
        produto.save()
        return redirect('cadastrar_produto')
    

def visualizar_produtos(request):
    return HttpResponse('pagina de visualização de protudos')
