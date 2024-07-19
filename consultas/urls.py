from django.urls import path
from .views import ConsultaViewSet


consulta_list = ConsultaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

consulta_detail = ConsultaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('consultas/', consulta_list, name='consulta-listar'),
    path('consultas/<int:pk>/', consulta_detail, name='consulta-detalhes'),
]
