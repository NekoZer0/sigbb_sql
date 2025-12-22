"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from produtos import views as produtos_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('produtos/', include('produtos.urls')),
    path('loja/', include('produtos.urls')),
    path('', produtos_views.index, name='index'),  # nova view para loja
    path('login/', produtos_views.login, name='login'),
    path('cadastrar_user/', produtos_views.cadastrar_user, name='cadastrar_user'),
]
