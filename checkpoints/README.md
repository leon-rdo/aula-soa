# Checkpoints — como voltar para o trilho

Travou? Perdeu um passo? Seu código quebrou e a aula seguiu?
**Não fique parado tentando consertar.** Pule para o checkpoint e volte para a aula.

Cada etapa virou uma tag no git. Todas foram testadas: extraídas num
diretório limpo, elas rodam.

## Tabela

| Tag | Aula | O que já existe nesse ponto |
|---|---|---|
| `cp0-inicio` | — | README, dependências e o exercício de consumo **com TODOs**. É onde você começa. |
| `cp1-consumo` | A1 · P2 | `consome_cep.py` completo: `timeout`, `raise_for_status()` e `try/except`. |
| `cp2-api-base` | A1 · P3a–b | Projeto Django + app `catalogo` + model `Produto` migrado. Só admin, ainda sem API. |
| `cp3-api-rest` | A1 · P3c–f | Serializer, ViewSet, router. `/api/produtos/` no ar, com `api.http`. |
| `cp-aula1-final` | A1 · P4 | Front em template consumindo a própria API. **Ponto de partida da aula 2.** |

As tags da aula 2 (`cp4-contrato` … `cp-aula2-final`) entram no dia 19.

## Como pular para um checkpoint

```
git stash                              # guarda o que você fez (não perde)
git switch -C resgate cp3-api-rest     # vai para o checkpoint
```

Pronto, você está no estado "tudo funcionando até o passo 3".

### Depois de pular, rode:

```
cd catalogo_service
python manage.py migrate
python manage.py loaddata produtos     # dados de exemplo (a partir do cp3)
python manage.py runserver 8001
```

> O banco (`db.sqlite3`) **não** está no git — ele é seu, local. Por isso
> trocar de tag não apaga seus dados, e por isso pode ser preciso rodar
> `migrate` depois de pular.

### Quero meu código de volta

```
git switch solucao     # ou o branch em que você estava
git stash pop          # devolve o que você tinha guardado
```

## Quer ver a solução de uma etapa?

O branch `solucao` tem a evolução completa, commit a commit:

```
git log --oneline solucao
git show cp3-api-rest
```

Não tem nota nesta aula. As soluções estão abertas de propósito — elas são
rede de segurança, não gabarito escondido.

## Git quebrou de vez?

Baixe o `.zip` do checkpoint pelo GitHub (botão **Code → Download ZIP** com a
tag selecionada) e continue por lá. Perder a aula por causa do git não vale a pena.
