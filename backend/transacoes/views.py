from rest_framework.decorators import api_view  # decorator que transforma uma função em view de API do DRF
from rest_framework.response import Response  # devolve o JSON e permite escolher o status code
from .models import Transacao  # importa o model para poder consultar o banco
from .serializers import TransacaoSerializer  # importa o serializer de transações


@api_view(['GET'])  # só aceita GET
def listar_transacoes(request):  # view que lista todas as transações
    transacoes = Transacao.objects.all()  # busca todas as transações no banco
    serializer = TransacaoSerializer(transacoes, many=True)  # traduz a lista de objetos para JSON (many=True: é uma lista)
    return Response(serializer.data)  # devolve o JSON com status 200


@api_view(['GET'])  # só aceita GET
def listar_transacoes_pendentes(request):  # view que lista só as transações pendentes
    transacoes = Transacao.objects.filter(status='PENDENTE')  # única diferença para a anterior: filter() traz só as de status PENDENTE
    serializer = TransacaoSerializer(transacoes, many=True)  # mesmo serializer; o formato do JSON não muda
    return Response(serializer.data)  # devolve o JSON com status 200


@api_view(['GET'])  # atividade parte 1: só aceita GET
def listar_transacoes_pagas(request):  # view que lista só as transações pagas
    transacoes = Transacao.objects.filter(status='PAGO')  # filter() traz só as de status PAGO
    serializer = TransacaoSerializer(transacoes, many=True)  # mesmo serializer
    return Response(serializer.data)  # devolve o JSON com status 200
