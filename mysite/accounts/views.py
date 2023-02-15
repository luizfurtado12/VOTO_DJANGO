from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from perguntas.models import Pergunta, Escolha
from perguntas.forms import FormPergunta, FormEscolha
from perguntas.views import IndexView, DetailView

# Create your views here.
class Dashboard(LoginRequiredMixin, IndexView):
    template_name: str = 'dashboard.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Pergunta.objects.filter(
            autor=self.request.user, mostra_opcoes=True
        ).order_by('-data')
        return qs

class DetalheView(LoginRequiredMixin, DetailView):
    template_name: str = 'detalhe_page.html'

    def get_queryset(self):
        return super().get_queryset()


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
        return redirect('accounts:perfil')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Usuario ou senha inválido'
        )
        return render(request, 'accounts_pages/login.html')


def adicionar_pergunta(request):
    template = render(request, 'forms/pergunta_form.html',
                      {'form': FormPergunta})
    if request.method == 'GET':
        return template

    if request.method == 'POST':
        text_polls = request.POST.get('texto_pergunta')

        if len(text_polls.strip()) < 1:
            messages.error(request, 'Campo não pode ser vazio')
            return template

        try:
            pergunta = Pergunta(
                texto_pergunta=text_polls,
                autor=request.user,
                data=timezone.now()
            )
            pergunta.save()
            messages.success(
                request, 'Pergunta foi feita com sucesso, adicione as opções')
            return redirect('accounts:fazer_escolhas')
        except Exception as e:
            messages.error(request, 'Erro interno')
            print(e)
            return template


def make_choice(request):
    polls = Pergunta.objects.filter(autor=request.user)
    template = render(request, 'forms/options_form.html',
                      {'choice': FormEscolha,
                       'polls': polls}
                      )

    if request.method == 'GET':
        return template

    if request.method == 'POST':
        options_text = request.POST.get('texto_escolha')
        pergunta_id = request.POST.get('perguntas')
        # escolhas = Escolha.objects.all()
        # perguntas = Pergunta.objects.filter(id=pergunta)
        # print(perguntas)

        if len(options_text.strip()) < 1:
            messages.error(request, 'Campo não pode ser vazio')
            return template
        if len(options_text.strip()) >= 200:
            messages.error(
                request, 'a opção tem que ser menor do que 200 caracteres')
            return template
        question = get_object_or_404(Pergunta, pk=pergunta_id)
        try:
            selected_choice = question.escolha_set.create(
                texto_escolha=options_text, votos=0)
            selected_choice.save()
            messages.success(request, 'Opção salvo com sucesso')
        except Exception as e:
            print(e)
            messages.error(request, 'Error interno, tente mais tarde')
        # messages.success(request, 'continua...')
        return redirect('accounts:fazer_escolhas')


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')
