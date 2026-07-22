import requests
from bs4 import BeautifulSoup
import json
import urllib.parse


def carregar_produtos():
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def buscar_google(termo):

    consulta = urllib.parse.quote(termo)

    url = f"https://www.google.com/search?q={consulta}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resposta = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    soup = BeautifulSoup(
        resposta.text,
        "html.parser"
    )

    resultados = []

    for item in soup.find_all("h3"):
        resultados.append(item.text)

    return resultados[:5]


def executar_busca():

    produtos = carregar_produtos()

    for produto in produtos:

        print("=" * 50)
        print(produto["nome"])

        resultados = buscar_google(produto["busca"])

        for resultado in resultados:
            print(resultado)


if __name__ == "__main__":
    executar_busca()
