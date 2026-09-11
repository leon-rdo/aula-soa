from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    """O CONTRATO do serviço de Catálogo.

    Este arquivo é a parte mais importante da aula de hoje.

    Um serializer faz duas coisas:
      1. traduz objeto Python -> JSON (o que sai na resposta);
      2. valida JSON -> objeto Python (o que entra no pedido).

    Tudo o que estiver aqui é promessa pública. Quem consumir sua API
    vai depender destes nomes de campo. Mudar "preco" para "valor"
    amanhã quebra o cliente de alguém. É por isso que chamamos de
    contrato, e é por isso que a aula 2 fala de versionamento.
    """

    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "preco", "disponivel", "criado_em"]
        # criado_em é gerado pelo servidor: o cliente não pode definir.
        read_only_fields = ["id", "criado_em"]

    def validate_preco(self, valor):
        """Validação de contrato: preço negativo não existe.

        Rejeitar aqui devolve 400 com uma mensagem clara, em vez de
        aceitar lixo e explodir em 500 mais tarde.
        """
        if valor <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return valor
