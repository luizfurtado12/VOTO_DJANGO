from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from .models import Pergunta, Escolha
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q


# Create your views here.
class IndexView(generic.ListView):
    model = Pergunta
    template_name: str = 'polls/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        # choice = Pergunta.options()
        qs = qs.filter(
            data__lte=timezone.now(), mostra_opcoes=True
        ).order_by('-data').select_related('autor')
        return qs


class SearchView(IndexView):
    template_name: str = 'polls/busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo') or self.request.session.get('termo')

        if not termo:
            return qs

        self.request.session['termo'] = termo
        qs = qs.filter(
            Q(texto_pergunta__icontains=termo)
        )
        self.request.session.save()
        return qs


class DetailView(generic.DetailView):
    model = Pergunta
    context_object_name: str = 'question'
    template_name: str = 'detalhes/index_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(data__lte=timezone.now(), mostra_opcoes=True).select_related()


class ResultsView(generic.DetailView):
    model = Pergunta
    context_object_name: str = 'question'
    template_name: str = 'polls/resultado.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(data__lte=timezone.now(), mostra_opcoes=True)


def votar(request, question_id):
    question = get_object_or_404(Pergunta, pk=question_id)

    if not question.mostra_opcoes:
        raise Http404('')

    try:
        selected_choice = question.escolha_set.get(  # type: ignore
            pk=request.POST['escolha'])
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
        return HttpResponseRedirect(reverse('perguntas:resultado', args=(question.id, )))  # type: ignore
