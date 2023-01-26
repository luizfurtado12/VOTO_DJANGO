from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='sair'),  # sempre retorna alguma coisa
    path('cadastrar-pergunta/', views.adicionar_pergunta, name='fazer_pergunta')
]
