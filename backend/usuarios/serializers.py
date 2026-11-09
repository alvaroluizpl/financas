from rest_framework import serializers  # importa as ferramentas de serializer do DRF
from .models import Usuario  # importa o model Usuario do próprio app


class UsuarioSerializer(serializers.ModelSerializer):  # serializer que monta os campos a partir do model Usuario
    class Meta:  # classe interna com as configurações do serializer
        model = Usuario  # de qual model vêm os dados
        fields = ['id', 'nome', 'email', 'data_cadastro']  # só estes campos saem no JSON; a senha NÃO está na lista, então nunca aparece
