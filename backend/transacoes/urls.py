from django.urls import path  # path liga um endereço (URL) a uma view
from .views import (  # importa as três views de transações
    listar_transacoes, listar_transacoes_pendentes, listar_transacoes_pagas,
)

urlpatterns = [  # lista de rotas deste app
    path('transacoes/', listar_transacoes),  # /api/transacoes/ lista todas
    path('transacoes/pendentes/', listar_transacoes_pendentes),  # /api/transacoes/pendentes/ lista só as PENDENTE
    path('transacoes/pagas/', listar_transacoes_pagas),  # /api/transacoes/pagas/ lista só as PAGO
]  # fecha a lista de rotas
