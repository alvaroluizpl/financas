from rest_framework.decorators import api_view  # decorator que transforma uma função em view de API do DRF
from rest_framework.response import Response  # devolve o JSON e permite escolher o status code (200, 404...)
from .models import Categoria  # importa o model para poder consultar o banco
from .serializers import CategoriaSerializer  # importa o serializer que traduz a categoria em JSON


@api_view(['GET'])  # esta view só aceita GET; outros verbos (POST, PUT...) recebem 405 Method Not Allowed
def listar_categorias(request):  # view que lista todas as categorias; request é a requisição HTTP recebida
    categorias = Categoria.objects.all()  # busca todas as categorias no banco (objetos, sem .values())
    serializer = CategoriaSerializer(categorias, many=True)  # entrega os objetos ao serializer; many=True avisa que é uma lista
    return Response(serializer.data)  # devolve os dados já traduzidos para JSON, com status 200 por padrão


@api_view(['GET'])  # atividade parte 2: também só aceita GET
def listar_categorias_despesas(request):  # view que lista só as categorias do tipo DESPESA
    categorias = Categoria.objects.filter(tipo='DESPESA')  # filter() traz só as categorias cujo tipo é DESPESA
    serializer = CategoriaSerializer(categorias, many=True)  # mesmo serializer; o formato do JSON não muda
    return Response(serializer.data)  # devolve o JSON com status 200
