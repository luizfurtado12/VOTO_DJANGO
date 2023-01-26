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
    # Verificar se o e-mail já está sendo usado por outro usuario
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_2 = request.POST.get('senha2')

    # Validação
    try:
        validate_email(email)
    except Exception as e:
        print(e)
        messages.error(request, 'E-mail inválido')
        return render(request, 'forms/cadastro_form.html')

    if len(nome.strip()) == 0 or len(sobrenome.strip()) == 0 or len(senha.strip()) == 0 or len(usuario.strip()) == 0:
        messages.error(request, 'Inválido')
        return render(request, 'forms/cadastro_form.html')
    if senha != senha_2:
        messages.error(request, 'ERROR: Senhas diferentes')
        return render(request, 'forms/cadastro_form.html')
    if len(usuario) <= 5:
        messages.error(
            request, 'ERROR: usuario precisa ter mais do que 5 caracteres')
        return render(request, 'forms/cadastro_form.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Nome de usuario já existe')
        return render(request, 'forms/cadastro_form.html')
    if User.objects.filter(email=email).exists():
        messages.error(
            request, 'E-mail já cadastro, tente outro endereço de E-mail')
        return render(request, 'forms/cadastro_form.html')

    try:
        user = User.objects.create_user(
            username=usuario,
            email=email,
            first_name=nome,
            last_name=sobrenome,
            password=senha,
        )
        user.save()
        messages.success(request, 'Usuario cadastro com sucesso')
        return redirect('accounts:login')
    except Exception as e:
        print(e)
        messages.error(request, 'Error interno, por favo tente mais tarde')
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


@login_required(redirect_field_name='accounts:login')
def adicionar_pergunta(request):
    template = render(request, 'forms/pergunta_form.html', {'form': FormPergunta})
    if request.method == 'GET':
        return template

    if request.method == 'POST':
        text_polls = request.POST.get('texto_pergunta')
        print(text_polls)
        messages.info(request, 'continua...')
        return template

# @staticmethod
# def form_valid(form):
#     pass

def dashboard(request):
    pass
