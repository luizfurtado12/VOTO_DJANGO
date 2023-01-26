from django.shortcuts import render, redirect
from django.contrib import auth, messages
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
    usuario = request.POST.get('usuario')  # tamanho
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_2 = request.POST.get('senha2')

    if len(nome.strip()) == 0 or len(sobrenome.strip()) == 0 or len(senha.strip()) == 0 or len(usuario.strip()) == 0:
        # print(nome.strip(), len(nome.strip()))
        # print(nome, sobrenome, usuario, email, senha, senha_2)
        messages.error(request, 'Inválido')
        return render(request, 'forms/cadastro_form.html')
    if not senha == senha_2:
        messages.error(request, 'ERROR: Senhas diferentes')
        return render(request, 'forms/cadastro_form.html')
    if len(usuario) <= 5:
        messages.error(request, 'ERROR: usuario precisa ter mais do que 5 caracteres')
        return render(request, 'forms/cadastro_form.html')

    messages.info(request, 'continuar...')
    return render(request, 'forms/cadastro_form.html')

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts_pages/login.html')

    usuario = request.POST.get('user')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if user:
        auth.login(request, user)
        messages.add_message(
            request,
            messages.SUCCESS,
            'logado com sucesso'
        )
        return redirect('perguntas:index')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Usuario ou senha inválido'
        )
        return render(request, 'accounts_pages/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def adicionar_pergunta(request):
    pass


def dashboard(request):
    pass
