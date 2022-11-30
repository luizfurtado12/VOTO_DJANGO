from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.utils import timezone
from django.views import generic

"""
    1° Mostrar apenas perguntas com respostas
"""
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now()).order_by('-date')[:10]


class DetailView(generic.DetailView):
    model = Question
    context_object_name: str = 'question'
    template_name: str = 'detalhes/index_detail.html'

    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now())


class ResultsView(generic.DeleteView):
    model = Question
    context_object_name: str = 'question'
    template_name: str = 'polls/resultado.html'

    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now())


def votar(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.escolha_set.get(pk=request.POST['escolha'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detalhes/index_detail.html', {
            'question': question,
            'error_message': "Selecione uma questão",
        })
    else:
        selected_choice.votos += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:resultado', args=(question.id, )))


""" codigo anterior:
def index(request):
    lista_perguntas = Pergunta.objects.order_by('-date')[:10]
    return render(request, 'polls/index.html',
                  {'lista_perguntas': lista_perguntas}
                  )

def detalhes(request, question_id):
    question = get_object_or_404(Pergunta, pk=question_id)
    return render(request, 'detalhes/index_detail.html', {'question': question})

def resultado(request, question_id):
    question = get_object_or_404(Pergunta, pk=question_id)
    return render(request, 'polls/resultado.html', {'question': question})
"""
