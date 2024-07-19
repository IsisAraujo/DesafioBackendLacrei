import logging
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

# Configurações de logging para o relatório
logging.basicConfig(filename='pessoa_profissional_test.log', level=logging.INFO)

class PessoaProfissionalTests(TestCase):
    def setUp(self):
        self.email = 'test@example.com'
        self.password = 'securepassword'
        self.nome_completo = 'Test User'
        self.profissao = 'MEDICO'
        self.endereco = '123 Test St'
        self.celular = '11987654321'
        self.nome_social = 'Test Social'
        self.cpf = '12345678901'
        self.especialidade_medica = 'CARDIOLOGIA'
        self.foto_documento = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

        # Criação do usuário para o teste
        self.user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
            nome_completo=self.nome_completo,
            profissao=self.profissao,
            endereco=self.endereco,
            celular=self.celular,
            nome_social=self.nome_social,
            cpf=self.cpf,
            especialidade_medica=self.especialidade_medica,
            foto_documento=self.foto_documento
        )

    def test_pessoa_profissional_creation(self):
        """Teste para garantir que o PessoaProfissional é criado corretamente"""
        user = get_user_model().objects.get(email=self.email)
        self.assertEqual(user.nome_completo, self.nome_completo)
        self.assertEqual(user.profissao, self.profissao)
        self.assertEqual(user.endereco, self.endereco)
        self.assertEqual(user.celular, self.celular)
        self.assertEqual(user.nome_social, self.nome_social)
        self.assertEqual(user.cpf, self.cpf)
        self.assertEqual(user.especialidade_medica, self.especialidade_medica)
        self.assertTrue(user.foto_documento)

        # Logando a criação do usuário
        logging.info(f'{datetime.now()} - PessoaProfissional criado com sucesso: {user}')

    def test_user_str_method(self):
        """Teste para garantir que o método __str__ retorna o nome social"""
        self.assertEqual(str(self.user), self.nome_social)
