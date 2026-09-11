from rest_framework import viewsets

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """Expõe o recurso /api/produtos/ com o CRUD completo.

    ModelViewSet entrega, de graça, as sete operações REST:

        GET    /api/produtos/       -> lista
        POST   /api/produtos/       -> cria
        GET    /api/produtos/{id}/  -> detalha
        PUT    /api/produtos/{id}/  -> substitui inteiro
        PATCH  /api/produtos/{id}/  -> altera um pedaço
        DELETE /api/produtos/{id}/  -> remove

    Repare que não existe /api/criarProduto/ nem /api/listarProdutos/.
    Em REST o substantivo está na URL e o verbo está no método HTTP.
    """

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
