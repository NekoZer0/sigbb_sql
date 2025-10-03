from turtle import st
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto


def cadastrar_produto(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastrar.html', {'status': status})

    elif request.method == 'POST':
        nome = request.POST.get('nome_do_produto')
        preco = request.POST.get('preco_do_produto')

        if float(preco) <= 0:
            # return redirect('/produtos/cadastrar/?status=0')
            return redirect('/loja/cadastrar/?status=0')

        produto = Produto(nome=nome, preco=preco)
        produto.save()

        # return redirect('/produtos/cadastrar/?status=1')
        return redirect('/loja/cadastrar/?status=1')


def visualizar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja.html', {'produtos': produtos})

def apagar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        return redirect('/loja/')
    except Produto.DoesNotExist:
        return HttpResponse("Produto não encontrado.", status=404)


def index(request):
    return render(request, 'index.html')  # Landpage


def loja(request):
    return render(request, 'loja.html')  # Exemplo
