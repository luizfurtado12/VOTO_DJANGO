from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Pergunta, Escolha


# Create your tests here.
class Options(TestCase):
    """
        vericando as opçoes das questões
    """
    def test_not_have_options_in_question(self):
        question_not_options = Pergunta.objects.create(texto_pergunta='sim ou não', data=timezone.now())
        self.assertIs(question_not_options.options(), False)

    def test_have_options_in_question(self):
        question = Pergunta.objects.create(texto_pergunta='sim ou não', data=timezone.now())
        question.escolha_set.create(texto_escolha='sim', votos=0)
        question.escolha_set.create(texto_escolha='não', votos=0)
        self.assertIs(question.options(), True)
