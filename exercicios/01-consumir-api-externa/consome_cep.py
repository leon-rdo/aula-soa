"""
Consumindo um serviço de terceiros: BrasilAPI (busca de CEP).

>>> ESTE ARQUIVO É O PONTO DE PARTIDA. Vamos completá-lo juntos na aula. <<<

O ponto NÃO é buscar CEP. O ponto é perceber que, do lado de cá,
um serviço é apenas: uma URL, um contrato de resposta e um monte
de coisa que pode dar errado.

Rodar:  python consome_cep.py
"""

import requests

BASE_URL = "https://brasilapi.com.br/api/cep/v2"

# Três CEPs escolhidos a dedo: cada um provoca um status HTTP diferente.
CEPS_DEMO = [
    ("66017000", "existe -> 200"),
    ("12345678", "nao encontrado -> 404"),
    ("1234", "formato invalido -> 400"),
]


def buscar_cep(cep):
    """Busca um CEP e devolve o dicionário do endereço."""
    # TODO 1: fazer o GET para f"{BASE_URL}/{cep}"
    # TODO 2: passar timeout=5  (por que isso não é opcional?)
    # TODO 3: chamar raise_for_status() (o que acontece sem ele num 404?)
    # TODO 4: devolver o .json()
    raise NotImplementedError("completar na aula")


def main():
    for cep, esperado in CEPS_DEMO:
        print(f"\n--- CEP {cep}  ({esperado}) ---")
        # TODO 5: envolver a chamada em try/except e tratar, separadamente:
        #           requests.HTTPError   -> o servidor disse "não"
        #           requests.Timeout     -> o servidor não respondeu
        #           requests.RequestException -> a rede falhou
        endereco = buscar_cep(cep)
        print(f"  {endereco['street']}, {endereco['neighborhood']}")
        print(f"  {endereco['city']}/{endereco['state']}")


if __name__ == "__main__":
    main()
