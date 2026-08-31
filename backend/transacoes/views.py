# JsonResponse converte dados Python em uma resposta HTTP em formato JSON.
from django.http import JsonResponse

# Importa o modelo Transacao deste mesmo app.
from .models import Transacao


def listar_transacoes(request):
    # Busca todas as transações, trazendo apenas os campos abaixo como
    # dicionários. Para as ForeignKeys (usuario, categoria), usamos
    # "usuario_id" e "categoria_id" para pegar só o ID relacionado,
    # em vez de trazer o objeto Usuario/Categoria inteiro.
    transacoes = Transacao.objects.all().values(
        'id', 'descricao', 'valor', 'data', 'tipo', 'status', 'usuario_id', 'categoria_id'
    )

    # Converte o QuerySet em lista e envia como resposta JSON.
    # safe=False permite serializar uma lista (não apenas dicionários).
    return JsonResponse(list(transacoes), safe=False)
