from rest_framework import viewsets  # módulo com os ViewSets, classes que já trazem o CRUD pronto
from .models import Usuario  # importa o model Usuario para consultar o banco
from .serializers import UsuarioSerializer  # importa o serializer que traduz e valida os usuários


class UsuarioViewSet(viewsets.ModelViewSet):  # classe que herda do ModelViewSet: listar, buscar, criar, editar (PUT/PATCH) e apagar
    queryset = Usuario.objects.all()  # de onde vêm os dados (nome fixo: é aqui que o DRF procura)
    serializer_class = UsuarioSerializer  # qual serializer usar para traduzir e validar (nome fixo também)
