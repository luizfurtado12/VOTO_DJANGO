from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
#  Muda a relação dos modelos
class Choice(models.Model):
    # link: https://docs.djangoproject.com/en/4.1/ref/models/fields/#foreignkey
    # pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    text_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.text_escolha


class Question(models.Model):
    texto_pergunta = models.CharField(max_length=255)
    date = models.DateTimeField('Data de publicação')
    escolha = models.ManyToManyField(  # Errado
        Choice,
        related_name='associacao',
        blank=True
    )

    def __str__(self):
        return self.texto_pergunta

    def publicado_recentemente(self):
        # return self.date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now
