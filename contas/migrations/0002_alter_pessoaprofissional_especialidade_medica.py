# Generated by Django 5.0.7 on 2024-07-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoaprofissional',
            name='especialidade_medica',
            field=models.CharField(choices=[('CARDIOLOGIA', 'Cardiologista'), ('DERMATOLOGIA', 'Dermatologista'), ('GINECOLOGIA', 'Ginecologista'), ('PEDIATRIA', 'Pediatra'), ('PSIQUIATRIA', 'Psiquiatra'), ('PSICOLOGIA', 'Psicologo'), ('OUTRO', 'Outro')], max_length=20),
        ),
    ]
