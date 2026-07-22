import requests
from bs4 import BeautifulSoup
import json
import urllib.parse


def carregar_produtos():
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def buscar_mercado_livre(termo):

    busca = urllib.parse.quote(termo)

    url = (
        "https://lista.mercadolivre.com.br/"
        + busca
    )

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

    produtos = soup.find_all(
        "h2",
        class_="poly-box__title"
    )

    for produto in produtos[:5]:
        resultados.append(
            produto.text.strip()
        )

    return resultados


def executar_busca():

    produtos = carregar_produtos()

    resultados_finais = []

    for produto in produtos:

        resultados = buscar_mercado_livre(
            produto["busca"]
        )

        resultados_finais.extend(resultados)

    return resultados_finais
