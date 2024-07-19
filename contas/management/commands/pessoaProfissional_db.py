from django.core.management.base import BaseCommand
from faker import Faker
from contas.models import PessoaProfissional, Profissao, EspecialidadeMedica

class Command(BaseCommand):
    help = 'Gera dados fictícios para o modelo PessoaProfissional'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')  # Define o local para gerar dados brasileiros

        # Definindo as opções para escolhas aleatórias
        profissoes = [profissao[0] for profissao in Profissao.choices]
        especialidades = [especialidade[0] for especialidade in EspecialidadeMedica.choices]

        for _ in range(5):
            cpf = fake.cpf().replace('.', '').replace('-', '')  # Remove pontuações do CPF

            # Gera um endereço fictício e ajusta o comprimento do campo celular para o formato correto
            endereco = fake.address()
            celular = fake.phone_number()
            if len(celular) > 11:
                celular = celular[:11]  # Ajusta para garantir que o número tenha 11 caracteres

            # Se necessário, ajuste o formato do número de telefone para se adequar ao modelo.
            # Exemplo de formatação: '11987654321'
            celular = celular.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

            # Cria uma instância do modelo PessoaProfissional
            user = PessoaProfissional(
                nome_completo=fake.name(),
                profissao=fake.random_element(profissoes),
                endereco=endereco,
                celular=celular,
                nome_social=fake.first_name(),
                email=fake.email(),
                cpf=cpf,
                especialidade_medica=fake.random_element(especialidades),
                foto_documento='fotos_documentos/placeholder_image.jpg',  
                is_active=True  # Definindo como ativo para facilitar os testes
            )
            user.set_password('django123')  # Define a senha para cada usuário
            user.save()

        self.stdout.write(self.style.SUCCESS('Dados fictícios criados com sucesso.'))
