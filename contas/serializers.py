from rest_framework import serializers
from .models import PessoaProfissional

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaProfissional
        fields = '__all__'
