from rest_framework.decorators import api_view  # decorator que transforma uma função em view de API do DRF
from rest_framework.response import Response  # devolve o JSON e permite escolher o status code
from .models import Usuario  # importa o model para poder consultar o banco
from .serializers import UsuarioSerializer  # importa o serializer que deixa a senha de fora


@api_view(['GET'])  # só aceita o verbo GET
def listar_usuarios(request):  # view que lista todos os usuários
    usuarios = Usuario.objects.all()  # busca todos os usuários no banco
    serializer = UsuarioSerializer(usuarios, many=True)  # traduz a lista de usuários; many=True porque são vários
    return Response(serializer.data)  # devolve o JSON com status 200


@api_view(['GET'])  # desafio: também só aceita GET
def buscar_usuario(request, id):  # view que busca um usuário; o id vem da URL (<int:id>)
    try:  # tenta buscar o usuário
        usuario = Usuario.objects.get(id=id)  # get() busca UM registro; se não existir, lança Usuario.DoesNotExist
    except Usuario.DoesNotExist:  # captura o erro de "não existe" em vez de deixar a API quebrar
        return Response({'erro': 'Usuário não encontrado'}, status=404)  # responde a mensagem de erro com o status 404
    serializer = UsuarioSerializer(usuario)  # sem many=True, porque é um objeto só
    return Response(serializer.data)  # devolve o JSON do usuário com status 200
