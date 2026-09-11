from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "disponivel", "criado_em")
    list_filter = ("disponivel",)
    search_fields = ("nome", "descricao")
