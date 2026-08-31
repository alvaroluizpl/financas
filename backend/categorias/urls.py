# "path" define uma rota (URL -> view).
from django.urls import path

# Importa o módulo views deste mesmo app.
from . import views

# Lista de rotas deste app, incluída em config/urls.py sob o prefixo
# "api/categorias/".
urlpatterns = [
    # Rota raiz do prefixo -> "api/categorias/", que chama a view
    # listar_categorias e recebe o apelido "listar_categorias".
    path('', views.listar_categorias, name='listar_categorias'),
]
