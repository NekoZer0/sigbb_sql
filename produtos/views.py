from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastrar_produto(request):
    return HttpResponse("Página de cadastro de produto.")

def cadastrar(request):
    return render(request, 'cadastrar_produto.html')