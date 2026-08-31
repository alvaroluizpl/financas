# "path" define uma rota (URL -> view).
from django.urls import path

# Importa o módulo views deste mesmo app.
from . import views

# Lista de rotas deste app, incluída em config/urls.py sob o prefixo
# "api/transacoes/".
urlpatterns = [
    # Rota raiz do prefixo -> "api/transacoes/", que chama a view
    # listar_transacoes e recebe o apelido "listar_transacoes".
    path('', views.listar_transacoes, name='listar_transacoes'),
]
