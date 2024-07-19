from rest_framework import viewsets
from django_filters import rest_framework as filters
from consultas.serializers import ConsultaSerializer
from consultas.models import Consulta

class ConsultaFilter(filters.FilterSet):
    medico_id = filters.NumberFilter(field_name='medico__id', lookup_expr='exact')

    class Meta:
        model = Consulta
        fields = ['medico_id']

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ConsultaFilter
