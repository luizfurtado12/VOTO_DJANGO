from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='sair'),  # sempre retorna alguma coisa
    path('cadastrar-pergunta/', login_required(views.adicionar_pergunta), name='fazer_pergunta'),
    path('cadastrar-escolha/', login_required(views.make_choice), name='fazer_escolhas'),
    path('suas-perguntas/', views.Dashboard.as_view(), name='perfil'),
    path('pergunta/<int:pk>/', views.DetalheView.as_view(), name='detail')
]
