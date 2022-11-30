from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detalhe'),
    # ex: /polls/5/
    path('<int:pk>/resultado/', views.ResultsView.as_view(), name='resultado'),
    # ex: /polls/5/resultado/
    path('<int:question_id>/votos/', views.votar, name='votos')
    # ex: /polls/5/votos/
]
