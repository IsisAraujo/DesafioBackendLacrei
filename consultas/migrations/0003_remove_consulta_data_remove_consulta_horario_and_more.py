# Generated by Django 5.0.7 on 2024-07-19 16:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_alter_consulta_especialidade_medica'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='data',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='pessoa_profissional',
        ),
        migrations.AlterField(
            model_name='consulta',
            name='nome_social_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to=settings.AUTH_USER_MODEL),
        ),
    ]
