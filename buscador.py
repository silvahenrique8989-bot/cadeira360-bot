import requests
import json
import urllib.parse
import xml.etree.ElementTree as ET


def carregar_produtos():

    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def buscar_google_rss(termo):

    busca = urllib.parse.quote(termo)

    url = (
        "https://news.google.com/rss/search?q="
        + busca
    )

    resposta = requests.get(
        url,
        timeout=10
    )

    resultados = []

    raiz = ET.fromstring(resposta.text)

    for item in raiz.findall(".//item")[:5]:

        titulo = item.find("title").text
        link = item.find("link").text

        resultados.append(
            f"{titulo}\n{link}"
        )

    return resultados


def executar_busca():

    produtos = carregar_produtos()

    resultados_finais = []

    for produto in produtos:

        resultados = buscar_google_rss(
            produto["busca"]
            + " preço promoção"
        )

        resultados_finais.extend(resultados)

    return resultados_finais
