from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProdutoViewSet

# O router cria todas as rotas do ViewSet a partir de uma linha.
router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet, basename="produto")

urlpatterns = [
    path("", include(router.urls)),
]
