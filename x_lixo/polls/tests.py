from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question, Choice
from django.urls import reverse

# Create your tests here.


class QuestionModelTest(TestCase):

    def publicado_recemente_no_futuro_teste(self):
        """
            was_published_recently() returns False for questions whose pub_date
        is in the future. A função retona falso para pergunta que está com date no futuro
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(date=time)
        self.assertiIs(future_question.publicado_recentemente(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day. Retorna False para publições que tem mais de 1 dia
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(date=time)
        self.assertIs(old_question.publicado_recentemente(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day. Retorna True para as publicções com menos de 1 dia
        retorna valores sensíveis de perguntas do passado, recente e futuro.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(date=time)
        self.assertIs(recent_question.publicado_recentemente(), True)


def create_question(question_text, dias):
    time = timezone.now() + datetime.timedelta(days=dias)
    return Question.objects.create(texto_pergunta=question_text, date=time)


class QuestionIndexViews(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Não a perguntas no momento!')
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_past_test(self):
        question = create_question(question_text='past question', dias=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        create_question(question_text='future question', dias=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'Não a perguntas no momento!')
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [],
        )

    def test_future_and_past(self):
        question = create_question(question_text='past question', dias=-30)
        create_question(question_text='future question', dias=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_question(self):
        question1 = create_question(question_text='past question 1', dias=-30)
        question2 = create_question(question_text='past question 2', dias=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )


class QuestionResultView(TestCase):
    def test_future_question(self):
        future_question = create_question(
            question_text='question in future', dias=17
        )
        url = reverse('polls:resultado', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class QuestionDetailView(TestCase):
    def test_future_question(self):
        future_question = create_question(
            question_text='question in fututre', dias=5)
        url = reverse('polls:detalhe', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_future(self):
        past_question = create_question(
            question_text='question in past', dias=-5)
        url = reverse('polls:detalhe', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.texto_pergunta)
