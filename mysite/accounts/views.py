from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from perguntas.forms import FormPergunta, FormEscolha

# Create your views here.
def login(request):
    return render(request, 'accounts_pages/login.html')

def logout(request):
    pass

def cadastro(request):
    pass

def adicionar_pergunta(request):
    pass

def dashboard(request):
    pass
