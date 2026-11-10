from rest_framework import viewsets  # módulo com os ViewSets, classes que já trazem o CRUD pronto
from rest_framework.decorators import action  # decorator que transforma um método do ViewSet em uma rota extra
from rest_framework.response import Response  # devolve o JSON com o status code
from .models import Categoria  # importa o model Categoria para consultar o banco
from .serializers import CategoriaSerializer  # importa o serializer que traduz e valida as categorias


class CategoriaViewSet(viewsets.ModelViewSet):  # herda do ModelViewSet: listar, buscar, criar, editar (PUT/PATCH) e apagar
    queryset = Categoria.objects.all()  # de onde vêm os dados (nome fixo: é aqui que o DRF procura)
    serializer_class = CategoriaSerializer  # qual serializer usar para traduzir e validar (nome fixo também)

    @action(detail=False, methods=['get'])  # rota extra da LISTA (detail=False): /categorias/despesas/, só aceita GET
    def despesas(self, request):  # o nome do método vira o final da URL
        categorias = Categoria.objects.filter(tipo='DESPESA')  # filter() traz só as categorias cujo tipo é DESPESA
        serializer = self.get_serializer(categorias, many=True)  # get_serializer usa o serializer_class do próprio ViewSet
        return Response(serializer.data)  # devolve o JSON com status 200
