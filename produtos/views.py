from turtle import st
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

def cadastrar_produto(request):
    if request.method == 'GET':
        status=request.GET.get('status')
        return render(request, 'cadastrar.html', {'status':status})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome_do_produto')
        preco = request.POST.get('preco_do_produto') 
             
        if float(preco)<=0:
            return redirect('/produtos/cadastrar/?status=0')  
        
        produto = Produto(nome=nome, preco=preco)
        produto.save()
        
        return redirect('/produtos/cadastrar/?status=1')  
    

def visualizar_produtos(request):
    return HttpResponse('pagina de visualização de protudos')
