from django.urls import path  # path liga um endereço (URL) a uma view
from .views import listar_usuarios, buscar_usuario  # importa as duas views de usuários

urlpatterns = [  # lista de rotas deste app
    path('usuarios/', listar_usuarios),  # /api/usuarios/ lista todos os usuários
    path('usuarios/<int:id>/', buscar_usuario),  # /api/usuarios/1/ busca um; <int:id> entrega o número da URL para a view no parâmetro id
]  # fecha a lista de rotas
