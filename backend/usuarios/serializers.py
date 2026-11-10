from django.contrib.auth.hashers import make_password  # função do Django que gera o hash de uma senha
from rest_framework import serializers  # importa as ferramentas de serializer do DRF
from .models import Usuario  # importa o model Usuario do próprio app


class UsuarioSerializer(serializers.ModelSerializer):  # serializer que monta os campos a partir do model Usuario
    class Meta:  # classe interna com as configurações do serializer
        model = Usuario  # de qual model vêm os dados
        fields = ['id', 'nome', 'email', 'senha', 'data_cadastro']  # a senha volta para a lista porque agora a API precisa RECEBER a senha para cadastrar
        extra_kwargs = {  # opções extras para campos que o ModelSerializer gera sozinho
            'senha': {'write_only': True},  # write_only: a API recebe a senha, mas NUNCA devolve no JSON
        }  # fecha o dicionário de opções

    def validate_senha(self, senha):  # o DRF chama este método sozinho para o campo "senha"
        return make_password(senha)  # troca a senha digitada pelo hash; é o hash que o save() grava no banco
