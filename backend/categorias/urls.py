from rest_framework.routers import SimpleRouter  # o Router cria as rotas do ViewSet sozinho
from .views import CategoriaViewSet  # importa o ViewSet de categorias

router = SimpleRouter()  # cria o router
router.register('categorias', CategoriaViewSet)  # gera categorias/ (lista), categorias/<id>/ (detalhe) e lê o @action (despesas)

urlpatterns = router.urls  # lista de rotas pronta; o Django procura por este nome
