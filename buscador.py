import requests
from bs4 import BeautifulSoup
import json
import urllib.parse


def carregar_produtos():
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def buscar_web(termo):

    consulta = urllib.parse.quote(termo)

    url = f"https://html.duckduckgo.com/html/?q={consulta}"

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

    links = soup.find_all(
        "a",
        class_="result__a"
    )

    for link in links[:5]:

        resultados.append(
            link.text
        )

    return resultados


def executar_busca():

    produtos = carregar_produtos()

    resultados_finais = []

    for produto in produtos:

        for site in produto["sites"]:

            termo = (
                produto["busca"]
                + " "
                + site
            )

            resultados = buscar_web(termo)

            resultados_finais.extend(resultados)

    return resultados_finais
