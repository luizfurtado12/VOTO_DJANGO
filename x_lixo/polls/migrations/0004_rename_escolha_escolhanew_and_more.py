# Generated by Django 4.1.2 on 2022-10-31 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_escolhanew_escolha_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Escolha',
            new_name='EscolhaNew',
        ),
        migrations.RenameModel(
            old_name='Pergunta',
            new_name='PerguntaNew',
        ),
    ]
