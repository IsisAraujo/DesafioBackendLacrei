# Generated by Django 5.0.7 on 2024-07-19 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0005_rename_nome_social_medico_consulta_medico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='especialidade_medica',
        ),
    ]
