from rest_framework import serializers  # importa as ferramentas de serializer do DRF (traduzem objeto Python <-> JSON)
from .models import Categoria  # importa o model Categoria do próprio app (o ponto significa "desta pasta")


class CategoriaSerializer(serializers.ModelSerializer):  # ModelSerializer monta os campos sozinho a partir do model
    class Meta:  # classe interna onde ficam as configurações do serializer
        model = Categoria  # de qual model (tabela) vêm os dados
        fields = ['id', 'nome', 'tipo']  # campos que aparecem no JSON e que podem ser recebidos

    def validate_nome(self, nome):  # validação personalizada: o DRF chama este método sozinho para o campo "nome"
        if len(nome) < 3:  # regra do nosso sistema: o nome precisa ter pelo menos 3 letras
            raise serializers.ValidationError('O nome precisa ter pelo menos 3 letras.')  # reprova: is_valid() vira False e a API responde 400 com esta mensagem
        return nome  # passou na regra: devolve o valor para o serializer continuar
