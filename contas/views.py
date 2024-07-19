import re
from rest_framework import viewsets, permissions, serializers

from contas.serializers import PessoaProfissionalSerializer
from .models import PessoaProfissional

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permissão personalizada que permite apenas ao próprio usuário ou a um admin 
    realizar atualizações e exclusões em um objeto.
    """
    def has_object_permission(self, request, view, obj):
        # Admins podem sempre acessar qualquer objeto
        if request.user.is_staff or request.user.is_superuser:
            return True
        # Usuários só podem acessar seus próprios objetos
        return obj == request.user

class PessoaProfissionalViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar as operações CRUD no modelo PessoaProfissional.
    """
    queryset = PessoaProfissional.objects.all()
    serializer_class = PessoaProfissionalSerializer

    def get_permissions(self):
        """
        Retorna as permissões apropriadas com base no método HTTP da solicitação.
        """
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwnerOrAdmin]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Sobrescreve o método para sanitizar o CPF antes de criar o objeto.
        """
        cpf = self.validate_cpf(serializer.validated_data.get('cpf', ''))
        serializer.validated_data['cpf'] = cpf
        super().perform_create(serializer)

    def validate_cpf(self, value):
        """
        Remove pontuações e valida o CPF.
        """
        cpf = re.sub(r'\D', '', value)  # Remove todos os caracteres não numéricos
        if len(cpf) != 11:
            raise serializers.ValidationError('CPF deve conter 11 dígitos.')
        return cpf
