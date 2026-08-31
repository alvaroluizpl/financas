# Importa o módulo "models" do Django, usado para definir tabelas do banco.
from django.db import models

# Importa os modelos de outros apps para poder relacioná-los aqui através
# de ForeignKey. Isso só funciona porque "usuarios" e "categorias" estão
# registrados em INSTALLED_APPS (config/settings.py).
from usuarios.models import Usuario
from categorias.models import Categoria


# Modelo que representa uma transação financeira (receita ou despesa).
class Transacao(models.Model):
    # Opções válidas para o campo "tipo": a transação é uma receita ou despesa.
    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]

    # Opções válidas para o campo "status": se a transação já foi paga ou não.
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
    ]

    # Texto curto descrevendo a transação, ex: "Conta de luz".
    descricao = models.CharField(max_length=200)

    # DecimalField é usado para valores monetários (evita erros de arredondamento
    # que aconteceriam com FloatField). max_digits=10 é o total de dígitos,
    # decimal_places=2 são as casas depois da vírgula (ex: 99999999.99).
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    # Data em que a transação ocorreu (sem horário).
    data = models.DateField()

    # Define se a transação é RECEITA ou DESPESA, usando as opções acima.
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    # Define se a transação está PENDENTE ou PAGA.
    # default='PENDENTE' faz esse ser o valor inicial caso nada seja informado.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')

    # ForeignKey cria um relacionamento "muitos para um": muitas transações
    # podem pertencer a um mesmo usuário. on_delete=models.CASCADE significa
    # que, se o usuário for excluído, todas as suas transações também serão.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    # Mesmo tipo de relacionamento, agora ligando a transação à sua categoria.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Representação em texto do objeto, ex: "Conta de luz - 150.00".
    def __str__(self):
        return f"{self.descricao} - {self.valor}"
