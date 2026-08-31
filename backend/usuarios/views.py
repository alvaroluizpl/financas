# JsonResponse é uma classe do Django que converte dados Python (dict/list)
# em uma resposta HTTP com corpo JSON e o header Content-Type correto.
from django.http import JsonResponse

# Importa o modelo Usuario deste mesmo app (import relativo com ".").
from .models import Usuario


# Toda view recebe pelo menos o parâmetro "request", com os dados da
# requisição HTTP (método, headers, parâmetros de busca, etc).
def listar_usuarios(request):
    # Usuario.objects.all() busca todos os registros da tabela de usuários.
    # .values(...) faz o banco retornar apenas os campos listados, já como
    # dicionários (em vez de objetos Usuario completos). Note que "senha"
    # foi propositalmente deixada de fora por segurança.
    usuarios = Usuario.objects.all().values('id', 'nome', 'email', 'data_cadastro')

    # .values() retorna um QuerySet (lazy); list() executa a consulta e
    # converte o resultado em uma lista de dicionários de verdade.
    # safe=False é necessário porque, por padrão, JsonResponse só aceita
    # dicionários na raiz — aqui estamos enviando uma lista.
    return JsonResponse(list(usuarios), safe=False)
