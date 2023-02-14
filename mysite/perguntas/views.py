from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Pergunta, Escolha
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q


# Create your views here.
class IndexView(generic.ListView):
    template_name: str = 'polls/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 5

    def get_queryset(self):
        # choice = Pergunta.options()
        pergunta = Pergunta.objects.filter(
            data__lte=timezone.now(), mostra_opcoes=True
        ).order_by('-data')
        return pergunta


class SearchView(IndexView):
    template_name: str = 'polls/busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        qs = Pergunta.objects.filter(
            Q(texto_pergunta__icontains=termo)
        )
        return qs


class DetailView(generic.DetailView):
    model = Pergunta
    context_object_name: str = 'question'
    template_name: str = 'detalhes/index_detail.html'

    def get_queryset(self):
        pergunta = Pergunta.objects.filter(
            data__lte=timezone.now(), mostra_opcoes=True)
        return pergunta

class ResultsView(generic.DeleteView):
    model = Pergunta
    context_object_name: str = 'question'
    template_name: str = 'polls/resultado.html'

    def get_queryset(self):
        return Pergunta.objects.filter(data__lte=timezone.now(), mostra_opcoes=True)

def votar(request, question_id):
    question = get_object_or_404(Pergunta, pk=question_id)
    try:
        selected_choice = question.escolha_set.get(pk=request.POST['escolha'])
    except (KeyError, Escolha.DoesNotExist):
        return render(
            request,
            'detalhes/index_detail.html', {
                'question': question,
                'error_message': "Selecione uma escolha",
            }
        )
    else:
        selected_choice.votos += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('perguntas:resultado', args=(question.id, )))
