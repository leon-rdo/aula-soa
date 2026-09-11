"""
Consumindo um serviço de terceiros: BrasilAPI (busca de CEP).

Este é o primeiro contato da aula com "consumir um serviço".
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
    """Busca um CEP e devolve o dicionário do endereço.

    Levanta requests.HTTPError para 4xx/5xx e requests.Timeout se o
    serviço demorar demais.
    """
    # timeout NUNCA é opcional ao chamar um serviço externo.
    # Sem ele, o seu programa fica refém do servidor do outro.
    resposta = requests.get(f"{BASE_URL}/{cep}", timeout=5)

    # Transforma 4xx/5xx em exceção. Sem isto, um 404 passaria
    # silenciosamente e você trataria uma mensagem de erro como se
    # fosse um endereço.
    resposta.raise_for_status()

    return resposta.json()


def main():
    for cep, esperado in CEPS_DEMO:
        print(f"\n--- CEP {cep}  ({esperado}) ---")
        try:
            endereco = buscar_cep(cep)
        except requests.HTTPError as erro:
            # O servidor respondeu, mas respondeu "não".
            print(f"  erro HTTP {erro.response.status_code}")
            print(f"  corpo: {erro.response.text[:120]}")
        except requests.Timeout:
            # O servidor não respondeu a tempo. É diferente de erro:
            # aqui você nem sabe se o pedido chegou.
            print("  o serviço não respondeu dentro de 5 segundos")
        except requests.RequestException as erro:
            # Rede caiu, DNS falhou, sem internet.
            print(f"  falha de rede: {erro}")
        else:
            print(f"  {endereco['street']}, {endereco['neighborhood']}")
            print(f"  {endereco['city']}/{endereco['state']}")


if __name__ == "__main__":
    main()
