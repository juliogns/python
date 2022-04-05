import email
from re import template
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import UpdateView


#Home
def home(request):
    return render(request, 'home.html')

#Formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')

#Inserção dos dados dos usuários no banco
def store(request):
    data={}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas não coincidem!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'], )
        user.first_name = request.POST['name']
        user.save()
        data['msg2'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-succes'

    return render(request, 'create.html', data)

#Formulário do painel de login
def painel(request):
    return render(request,'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html',data)

#Processa o logout
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

#Formulário de troca de senha
def changePasswordPanel(request):
    return render(request, 'dashboard/change-password-panel.html')

#Processa troca de senha
def changePassword(request):
    data={}
    if(request.POST['new_password1'] != request.POST['new_password2']):
        data['msg'] = 'As senhas não coincidem!'
        data['class'] = 'alert-danger'
        return render(request, 'dashboard/change-password-panel.html', data)
    else:
        user = User.objects.get(email=request.user.email)
        user.set_password(request.POST['new_password1'])
        user.save()
        logout(request)
        return redirect('/painel/')

