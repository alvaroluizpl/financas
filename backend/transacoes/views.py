from rest_framework import viewsets  # módulo com os ViewSets (CRUD pronto)
from rest_framework.decorators import action  # decorator que transforma um método do ViewSet em uma rota extra
from rest_framework.response import Response  # devolve o JSON com o status code
from .models import Transacao  # importa o model para consultar o banco
from .serializers import TransacaoSerializer  # importa o serializer de transações


class TransacaoViewSet(viewsets.ModelViewSet):  # herda do ModelViewSet: já faz listar, buscar, criar, editar e apagar
    queryset = Transacao.objects.all()  # de onde vêm os dados (nome fixo)
    serializer_class = TransacaoSerializer  # qual serializer usar (nome fixo)

    def get_queryset(self):  # sobrescreve o método que o ViewSet chama para saber QUAIS dados usar
        transacoes = Transacao.objects.all()  # começa com todas as transações
        tipo = self.request.query_params.get('tipo')  # lê o ?tipo= da URL (devolve None se não vier)
        if tipo:  # se veio o filtro...
            transacoes = transacoes.filter(tipo=tipo.upper())  # filtra pelo tipo; upper() faz ?tipo=receita funcionar também
        return transacoes  # devolve a lista (filtrada ou completa)

    @action(detail=False, methods=['get'])  # rota extra da LISTA (detail=False): /transacoes/pendentes/, só aceita GET
    def pendentes(self, request):  # o nome do método vira o final da URL
        transacoes = Transacao.objects.filter(status='PENDENTE')  # só as transações com status PENDENTE (este atalho ignora o ?tipo=)
        serializer = self.get_serializer(transacoes, many=True)  # get_serializer usa o serializer_class do próprio ViewSet
        return Response(serializer.data)  # devolve o JSON com status 200

    @action(detail=False, methods=['get'])  # rota extra: /transacoes/pagas/, só aceita GET
    def pagas(self, request):  # o nome do método vira o final da URL
        transacoes = Transacao.objects.filter(status='PAGO')  # só as transações com status PAGO
        serializer = self.get_serializer(transacoes, many=True)  # traduz a lista para JSON
        return Response(serializer.data)  # devolve o JSON com status 200
