from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=255)
    data = models.DateTimeField('Data da Publicação')
    mostra_opcoes = models.BooleanField(default=False)

    def __str__(self):
        return self.texto_pergunta

    def publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data <= now


class Escolha(models.Model):
    # Object.escolha_set.count()=0 | para nenhuma resposta
    texto_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_escolha
