# Generated by Django 4.1.2 on 2023-01-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0002_pergunta_mostra_opcoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='mostra_opcoes',
            field=models.BooleanField(default=False),
        ),
    ]
