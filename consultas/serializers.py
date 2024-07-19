from rest_framework import serializers

from consultas.models import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    medico_nome_social = serializers.CharField(source='medico.nome_social', read_only=True)
    especialidade_medica = serializers.CharField(source='medico.especialidade_medica', read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'especialidade_medica', 'valor', 'data', 'medico_nome_social']
