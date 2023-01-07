from django.forms import ModelForm
from .models import Pergunta, Escolha

class FormPergunta(ModelForm):
    class Meta:
        model = Pergunta
        fields = ('texto_pergunta',)
