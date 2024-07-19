from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from contas.models import PessoaProfissional

class Consulta(models.Model):
    medico = models.ForeignKey(PessoaProfissional, on_delete=models.SET_NULL, null=True, related_name='consultas')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = _('Consulta')
        verbose_name_plural = _('Consultas')

    def __str__(self):
        return f'{self.medico.nome_social} - {self.valor}'
