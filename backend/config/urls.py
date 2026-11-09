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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # /admin/ abre o Django Admin
    path('api/', include('usuarios.urls')),  # tudo que vem depois de /api/ é entregue ao urls.py de usuarios (include "puxa" as rotas do app)
    path('api/', include('categorias.urls')),  # idem para categorias; o Django tenta cada lista, na ordem, até achar a rota
    path('api/', include('transacoes.urls')),  # idem para transações
]
