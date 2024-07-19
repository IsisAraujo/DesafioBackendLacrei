from django.core.management.base import BaseCommand
from django.utils import timezone
from random import choice, uniform
from faker import Faker

from contas.models import PessoaProfissional
from consultas.models import Consulta

class Command(BaseCommand):
    help = 'Cria 5 consultas com médicos aleatórios'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Obtém todos os médicos existentes
        profissionais = PessoaProfissional.objects.all()

        if not profissionais:
            self.stdout.write(self.style.ERROR('Nenhum profissional encontrado.'))
            return
        
        for _ in range(5):
            medico = choice(profissionais)
            valor = round(uniform(100, 300), 2)
            data = fake.date_this_year()

            Consulta.objects.create(
                medico=medico,
                valor=valor,
                data=data
            )
        
        self.stdout.write(self.style.SUCCESS('5 consultas criadas com sucesso.'))
