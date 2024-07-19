from rest_framework import serializers
from .models import PessoaProfissional

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaProfissional
        fields = [
            'nome_completo',
            'profissao',
            'endereco',
            'celular',
            'nome_social',
            'email',
            'cpf',
            'especialidade_medica',
            'foto_documento',
        ]
