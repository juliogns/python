"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.views import changePassword, changePasswordPanel, home, create, store, painel, dologin, dashboard, logouts, cadastro, editarCadastro, DadosCreate, AdrCreate, DadosUpdate, AdrUpdate

urlpatterns = [
    path('dados/', DadosCreate.as_view(), name='dados-campo'),
    path('endereco/', AdrCreate.as_view(), name='endereco-campo'),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', create),
    path('cadastro/', cadastro),
    path('editar-cadastro/', editarCadastro),
    path('store/', store),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard, name='dashboard'),
    path('logouts/', logouts),
    path('password/', changePassword),
    path('password-panel/', changePasswordPanel),

    path('editar-dados/<int:pk>/', DadosUpdate.as_view(), name='editar-dados'),
    path('editar-endereco/<int:pk>/', AdrUpdate.as_view(), name='editar-endereco'),
]
