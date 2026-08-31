"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# admin.site.urls contém todas as rotas prontas da interface administrativa
# do Django (/admin/).
from django.contrib import admin

# path define uma rota. include permite "plugar" o urls.py de outro app
# dentro de um prefixo, delegando o roteamento para aquele app.
from django.urls import path, include

# Roteador principal do projeto: toda requisição passa primeiro por aqui.
urlpatterns = [
    # Todas as URLs que começam com "admin/" vão para o painel administrativo.
    path('admin/', admin.site.urls),

    # Toda URL que começa com "api/usuarios/" é delegada para o
    # usuarios/urls.py, que decide o que fazer com o restante do caminho.
    path('api/usuarios/', include('usuarios.urls')),

    # Mesma ideia, agora para o app de categorias.
    path('api/categorias/', include('categorias.urls')),

    # Mesma ideia, agora para o app de transações.
    path('api/transacoes/', include('transacoes.urls')),
]
