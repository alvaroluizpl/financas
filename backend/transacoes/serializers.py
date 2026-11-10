from rest_framework import serializers  # importa as ferramentas de serializer do DRF
from .models import Transacao  # importa o model Transacao do próprio app


class TransacaoSerializer(serializers.ModelSerializer):  # serializer baseado no model Transacao
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)  # campo novo (não existe no model): source diz de onde buscar o valor; read_only: só aparece na resposta
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)  # mesma ideia: entra na categoria da transação e pega o nome

    class Meta:  # classe interna com as configurações do serializer
        model = Transacao  # de qual model vêm os dados
        fields = [  # campos que aparecem no JSON
            'id', 'descricao', 'valor', 'data', 'tipo', 'status',  # campos do próprio model (valor sai como texto: "250.00")
            'usuario', 'usuario_nome', 'categoria', 'categoria_nome',  # o id continua sendo usado para cadastrar; o nome só facilita a leitura
        ]  # fecha a lista de campos

    def validate_valor(self, valor):  # validação de UM campo: o DRF chama sozinho para "valor"
        if valor <= 0:  # o model aceita valor negativo, mas no nosso sistema isso não faz sentido
            raise serializers.ValidationError('O valor precisa ser maior que zero.')  # reprova: a API responde 400 com esta mensagem
        return valor  # passou na regra: devolve o valor

    def validate(self, dados):  # validação de VÁRIOS campos juntos: recebe todos os dados de uma vez
        categoria = dados.get('categoria')  # objeto Categoria enviado (None se não veio, como no PATCH)
        tipo = dados.get('tipo')  # tipo enviado (None se não veio)
        # no PATCH, o campo que não veio continua com o valor já salvo
        if self.instance:  # no PUT e no PATCH, instance é a transação que já está salva (na criação é None)
            categoria = categoria or self.instance.categoria  # se não veio categoria, usa a que já estava salva
            tipo = tipo or self.instance.tipo  # se não veio tipo, usa o que já estava salvo
        if categoria.tipo != tipo:  # regra de negócio: o tipo da transação precisa ser igual ao tipo da categoria
            raise serializers.ValidationError(  # reprova: a API responde 400 com a mensagem abaixo
                'O tipo da transação precisa ser igual ao tipo da categoria.')  # o erro aparece em "non_field_errors"
        return dados  # passou na regra: devolve os dados
