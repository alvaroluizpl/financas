from rest_framework.routers import SimpleRouter  # o Router cria as rotas do ViewSet sozinho
from .views import UsuarioViewSet  # importa o ViewSet de usuários

router = SimpleRouter()  # cria o router
router.register('usuarios', UsuarioViewSet)  # "o recurso usuarios é atendido por este ViewSet": gera usuarios/ (lista) e usuarios/<id>/ (detalhe)

urlpatterns = router.urls  # router.urls é a lista de rotas pronta; o Django procura por este nome
