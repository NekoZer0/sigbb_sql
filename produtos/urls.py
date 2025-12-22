from django.urls import path
from produtos import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'), # type: ignore
    path('login/', views.login, name='login'),
    path('cadastrar_user/', views.cadastrar_user, name='cadastrar_user'),
    path('', views.visualizar_produtos, name='visualizar_produtos'),
    path('apagar_produto/<int:produto_id>/', views.apagar_produto, name='apagar_produto'),     # nova rota para apagar produto
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'), # nova rota para editar produto # type: ignore
          
]
