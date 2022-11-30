# Generated by Django 4.1.2 on 2022-10-21 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pergunta', models.CharField(max_length=255)),
                ('date', models.DateTimeField(verbose_name='Data de publicação')),
            ],
        ),
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_escolha', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pergunta')),
            ],
        ),
    ]
