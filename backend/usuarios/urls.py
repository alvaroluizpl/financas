# "path" define uma rota (URL -> view). "include" é usado no urls.py
# principal para importar essas rotas dentro de outro prefixo.
from django.urls import path

# Importa o módulo views deste mesmo app (import relativo com ".").
from . import views

# Lista de rotas deste app. Ela é "incluída" dentro de config/urls.py
# sob o prefixo "api/usuarios/".
urlpatterns = [
    # path('', ...) casa com a própria raiz do prefixo, ou seja,
    # com "api/usuarios/" exatamente. "name" dá um apelido à rota,
    # útil para gerar URLs no código sem escrever o caminho na mão.
    path('', views.listar_usuarios, name='listar_usuarios'),
]
