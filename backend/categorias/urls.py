from django.urls import path  # path liga um endereço (URL) a uma view
from .views import listar_categorias, listar_categorias_despesas  # importa as duas views de categorias

urlpatterns = [  # lista de rotas deste app (o Django procura exatamente por este nome)
    path('categorias/', listar_categorias),  # /api/categorias/ chama listar_categorias (o "api/" vem do config/urls.py)
    path('categorias/despesas/', listar_categorias_despesas),  # /api/categorias/despesas/ lista só as de DESPESA
]  
