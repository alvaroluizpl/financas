from rest_framework.routers import SimpleRouter  # o Router cria as rotas do ViewSet sozinho
from .views import TransacaoViewSet  # importa o ViewSet de transações

router = SimpleRouter()  # cria o router
router.register('transacoes', TransacaoViewSet)  # gera transacoes/ e transacoes/<id>/ e também lê os @action (pendentes e pagas)

urlpatterns = router.urls  # lista de rotas pronta; não precisamos mais escrever pendentes e pagas na mão
