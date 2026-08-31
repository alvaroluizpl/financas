# JsonResponse converte dados Python em uma resposta HTTP em formato JSON.
from django.http import JsonResponse

# Importa o modelo Categoria deste mesmo app.
from .models import Categoria


def listar_categorias(request):
    # Busca todas as categorias, retornando apenas os campos id, nome e tipo
    # já como dicionários, em vez de objetos Categoria completos.
    categorias = Categoria.objects.all().values('id', 'nome', 'tipo')

    # Converte o QuerySet em lista e envia como resposta JSON.
    # safe=False permite serializar uma lista (não apenas dicionários).
    return JsonResponse(list(categorias), safe=False)
