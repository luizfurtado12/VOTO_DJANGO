from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from perguntas.forms import FormPergunta, FormEscolha

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'forms/cadastro_form.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_2 = request.POST.get('senha2')
    # print(nome, sobrenome, usuario, email, senha, senha_2)
    return render(request, 'forms/cadastro_form.html')

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts_pages/login.html')

    usuario = request.POST.get('user')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if user:
        return redirect('perguntas:index')
    else:
        return redirect('accounts:login')


def logout(request):
    auth.logout(request)
    return redirect('login')


def adicionar_pergunta(request):
    pass


def dashboard(request):
    pass
