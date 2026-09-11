# Arquitetura Orientada a Serviços — projeto das aulas

Pós-graduação · aulas de **12/09** e **19/09/2026**, 08h–12h, online.

Construímos dois serviços que conversam por HTTP:

| Serviço | Porta | O que faz |
|---|---|---|
| `catalogo_service` | **8001** | Dono dos produtos. Aula 1. |
| `pedidos_service` | **8002** | Registra pedidos consultando o Catálogo. Aula 2. |
| `frontend/` | **8080** | Página que consome os dois. Aula 2. |

**Use exatamente essas portas.** Metade dos problemas de aula online é "na minha deu outra porta".

---

## Preparar o ambiente (faça antes da aula)

### 1. Clonar

```
git clone <URL-DO-REPOSITORIO>
cd projeto
```

### 2. Criar o ambiente virtual

**Windows (PowerShell ou cmd):**
```
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```
python3 -m venv .venv
source .venv/bin/activate
```

> Deu certo? O seu terminal passa a mostrar `(.venv)` no começo da linha.
> **Toda** vez que abrir um terminal novo você precisa ativar de novo.

> **Windows reclamando de "execução de scripts foi desabilitada"?**
> Use o `cmd` em vez do PowerShell, ou rode uma única vez:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

### 3. Instalar as dependências

```
pip install -r requirements.txt
```

### 4. Conferir

```
python -c "import django, rest_framework, requests; print(django.get_version())"
```

Deve imprimir `5.2.x`. Se imprimiu, você está pronto.

---

## Aula 1 — 12/09

### Exercício de consumo

```
python exercicios/01-consumir-api-externa/consome_cep.py
```

### Subir o serviço de Catálogo

```
cd catalogo_service
python manage.py migrate
python manage.py runserver 8001
```

Depois abra:

| Endereço | O que é |
|---|---|
| http://127.0.0.1:8001/ | O front que consome a API |
| http://127.0.0.1:8001/api/produtos/ | A API (browsable API do DRF) |
| http://127.0.0.1:8001/admin/ | Admin do Django |

**Precisa de dados de exemplo?**
```
python manage.py loaddata produtos
```

**Precisa entrar no admin?** Crie seu usuário:
```
python manage.py createsuperuser
```

> O banco é SQLite e fica no seu computador. Nada aqui vai para produção,
> então senha fraca em aula não é problema — **fora da aula, é**.

---

## Se você se perder no meio da aula

Cada etapa da aula virou uma **tag** no git. Para pular direto para o
estado "tudo pronto até o passo X", veja [`checkpoints/README.md`](checkpoints/README.md).

---

## Estrutura

```
projeto/
├── requirements.txt            # aula 1
├── requirements-aula2.txt      # aula 2 (instalar só no dia 19)
├── exercicios/
│   └── 01-consumir-api-externa/
│       ├── consome_cep.py      # consumindo serviço de terceiro
│       └── requests.http       # as mesmas chamadas, sem Python
├── catalogo_service/           # SERVIÇO A — porta 8001
│   ├── manage.py
│   ├── api.http                # chamadas prontas para o REST Client
│   ├── catalogo/               # app de domínio
│   │   ├── models.py           # Produto
│   │   ├── serializers.py      # o CONTRATO
│   │   ├── views.py            # ProdutoViewSet
│   │   └── urls.py             # DefaultRouter
│   └── frontend/templates/
│       └── index.html          # HTML + fetch, servido pelo Django
└── checkpoints/
    └── README.md
```
