import requests
import json
import urllib.parse


def carregar_produtos():

    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def buscar_mercado_livre(termo):

    busca = urllib.parse.quote(termo)

    url = (
        "https://api.mercadolibre.com/sites/MLB/search?q="
        + busca
    )

    resposta = requests.get(url, timeout=10)

    dados = resposta.json()
    
    print(dados)
    
    resultados = []

    for item in dados.get("results", [])[:5]:

        titulo = item["title"]
        preco = item["price"]
        link = item["permalink"]

        resultados.append(
            f"{titulo}\nR$ {preco:.2f}\n{link}"
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
