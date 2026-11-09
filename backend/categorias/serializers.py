from rest_framework import serializers  # importa as ferramentas de serializer do DRF (traduzem objeto Python <-> JSON)
from .models import Categoria  # importa o model Categoria do próprio app (o ponto significa "desta pasta")


class CategoriaSerializer(serializers.ModelSerializer):  # ModelSerializer monta os campos sozinho a partir do model
    class Meta:  # classe interna onde ficam as configurações do serializer
        model = Categoria  # de qual model (tabela) vêm os dados
        fields = ['id', 'nome', 'tipo']  # campos que vão aparecer no JSON (listar os campos é escolher o que a API mostra)
