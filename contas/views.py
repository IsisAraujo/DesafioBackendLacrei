
from rest_framework import viewsets, permissions

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

