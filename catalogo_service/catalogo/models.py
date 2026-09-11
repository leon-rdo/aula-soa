from django.db import models


class Produto(models.Model):
    """Um item do catálogo.

    Este model é o coração do serviço de Catálogo. Repare no que ele
    NÃO tem: nenhuma referência a pedido, cliente ou estoque. Catálogo
    sabe de produto. Só. Essa fronteira é a arquitetura.
    """

    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.nome
