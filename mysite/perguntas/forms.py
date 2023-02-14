from django.forms import ModelForm
from .models import Pergunta, Escolha

class FormPergunta(ModelForm):

    class Meta:
        model = Pergunta
        fields = ('texto_pergunta',)

class FormEscolha(ModelForm):
    class Meta:
        model = Escolha
        fields = ('texto_escolha',)
