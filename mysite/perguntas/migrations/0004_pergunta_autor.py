# Generated by Django 4.1.2 on 2023-01-26 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perguntas', '0003_alter_pergunta_mostra_opcoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
