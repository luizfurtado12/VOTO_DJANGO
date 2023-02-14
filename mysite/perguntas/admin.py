from django.contrib import admin
from .models import Pergunta, Escolha

# Register your models here.


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto_pergunta', 'data', 'autor', 'mostra_opcoes')
    list_display_links = ('id', 'texto_pergunta')
    list_editable = ('mostra_opcoes',)
    list_filter = ('data', )
    search_fields = ('texto_pergunta', )


admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Escolha)
