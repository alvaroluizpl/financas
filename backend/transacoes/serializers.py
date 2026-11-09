from rest_framework import serializers  # importa as ferramentas de serializer do DRF
from .models import Transacao  # importa o model Transacao do próprio app


class TransacaoSerializer(serializers.ModelSerializer):  # serializer baseado no model Transacao
    class Meta:  # classe interna com as configurações do serializer
        model = Transacao  # de qual model vêm os dados
        fields = [  # campos que vão aparecer no JSON
            'id', 'descricao', 'valor', 'data',  # id, texto, valor (sai como texto "250.00" para não perder precisão) e data (AAAA-MM-DD)
            'tipo', 'status', 'usuario', 'categoria',  # RECEITA/DESPESA, PENDENTE/PAGO e as chaves estrangeiras (aparecem como id)
        ]  # fecha a lista de campos
