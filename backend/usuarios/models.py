# Importa o módulo "models" do Django, que fornece a classe base
# para criar tabelas do banco de dados usando Python (ORM).
from django.db import models


# Toda tabela do banco vira uma classe que herda de models.Model.
# O Django usa essa classe para gerar automaticamente a tabela "usuarios_usuario".
class Usuario(models.Model):
    # CharField = coluna de texto curto. max_length define o limite de caracteres.
    nome = models.CharField(max_length=100)

    # EmailField = CharField especializado que já valida formato de e-mail.
    # unique=True impede que dois usuários se cadastrem com o mesmo e-mail.
    email = models.EmailField(unique=True)

    # Guarda a senha do usuário. Em produção, NUNCA salve senha em texto puro:
    # o ideal é usar hashing (ex: django.contrib.auth.hashers.make_password).
    senha = models.CharField(max_length=128)

    # DateTimeField = coluna de data e hora.
    # auto_now_add=True faz o Django preencher automaticamente com o momento
    # da criação do registro, sem precisar informar esse valor manualmente.
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # __str__ define como o objeto aparece quando é impresso ou exibido
    # no Django Admin. Aqui, mostramos o nome do usuário em vez de "Usuario object (1)".
    def __str__(self):
        return self.nome
