from django.forms import ModelForm
from .models import Pergunta, Escolha

class FormPergunta(ModelForm):
    def clean(self):
        data = self.changed_data
        texto = data.get('texto_pergunta')

        if len(texto.strip()) == 0:
            self.add_error(
                'texto_pergunta',
                'Pergunta inválida'
            )

    class Meta:
        model = Pergunta
        fields = ('texto_pergunta',)

class FormEscolha(ModelForm):
    class Meta:
        model = Escolha
        fields = ('texto_escolha',)
