from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

#Formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')

#Inserção dos dados dos usuários no banco
def store(request):
    data={}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'

    return render(request, 'create.html', data)

