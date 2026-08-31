# Importa o módulo "models" do Django, usado para definir tabelas do banco.
from django.db import models


# Modelo que representa uma categoria de transação (ex: "Alimentação", "Salário").
class Categoria(models.Model):
    # TIPO_CHOICES define as opções válidas para o campo "tipo" logo abaixo.
    # Cada item é uma tupla: (valor salvo no banco, texto exibido para humanos).
    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]

    # Nome da categoria, ex: "Transporte".
    nome = models.CharField(max_length=100)

    # Campo de texto restrito às opções de TIPO_CHOICES.
    # O Django valida automaticamente que só "RECEITA" ou "DESPESA" sejam salvos.
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    # Representação em texto do objeto, usada no admin e em prints/debug.
    # f-string monta algo como: "Transporte (DESPESA)".
    def __str__(self):
        return f"{self.nome} ({self.tipo})"
