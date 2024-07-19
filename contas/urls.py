from django.urls import path

from .views import PessoaProfissionalViewSet



urlpatterns = [
    path('profissionais/', PessoaProfissionalViewSet.as_view({'get': 'list'}), name='profissional-listar'),
    path('profissionais/cadastrar/', PessoaProfissionalViewSet.as_view({'post': 'create'}), name='profissional-cadastrar'),
    path('profissionais/<int:pk>/atualizar/', PessoaProfissionalViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name='profissional-atualizar'),
    path('profissionais/<int:pk>/excluir/', PessoaProfissionalViewSet.as_view({'delete': 'destroy'}), name='profissional-excluir'),
] 
