import logging
from django.test import TestCase
from django.utils import timezone
from contas.models import PessoaProfissional
from .models import Consulta

# Configurações de logging para o relatório
logging.basicConfig(filename='consulta_test.log', level=logging.INFO)

class ConsultaTests(TestCase):
    def setUp(self):
        # Configuração de dados para o teste
        self.medico = PessoaProfissional.objects.create(
            email='medico@example.com',
            password='securepassword',
            nome_completo='Dr. Test',
            profissao='MEDICO',
            endereco='456 Medical Rd',
            celular='11987654321',
            nome_social='Dr. Test',
            cpf='98765432100',
            especialidade_medica='CARDIOLOGIA',
            foto_documento=None  # Você pode ajustar conforme necessário
        )
        self.valor = 150.00
        self.data = timezone.now().date()

        # Criação de uma consulta para o teste
        self.consulta = Consulta.objects.create(
            medico=self.medico,
            valor=self.valor,
            data=self.data
        )

    def test_consulta_creation(self):
        """Teste para garantir que a Consulta é criada corretamente"""
        consulta = Consulta.objects.get(medico=self.medico)
        self.assertEqual(consulta.medico, self.medico)
        self.assertEqual(consulta.valor, self.valor)
        self.assertEqual(consulta.data, self.data)

        # Logando a criação da consulta
        logging.info(f'{timezone.now()} - Consulta criada com sucesso: {consulta}')

    def test_consulta_str_method(self):
        """Teste para garantir que o método __str__ retorna o nome do médico e o valor da consulta"""
        self.assertEqual(str(self.consulta), f'{self.medico.nome_social} - {self.valor}')
