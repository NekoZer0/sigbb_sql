from django.urls import path
from produtos import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'), # type: ignore
    path('visualizar/', views.visualizar_produtos, name='visualizar_produtos'),
    path('', views.index, name='index'), # type: ignore

]
