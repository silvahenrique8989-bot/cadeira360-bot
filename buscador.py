import json
from urllib.parse import quote_plus


SITES = [
    "pelando.com.br",
    "promobit.com.br"
]


def carregar_produtos():

    with open("produtos.json", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def gerar_buscas():

    produtos = carregar_produtos()

    resultado = []

    for produto in produtos:

        buscas = []

        for pesquisa in produto["pesquisas"]:

            for site in SITES:

                consulta = f"site:{site} {pesquisa}"

                link = (
                    "https://www.google.com/search?q="
                    + quote_plus(consulta)
                )

                buscas.append({
                    "site": site,
                    "pesquisa": pesquisa.replace('"', ''),
                    "link": link
                })

        resultado.append({

            "produto": produto["nome"],

            "preco_excelente": produto["preco_excelente"],

            "preco_bom": produto["preco_bom"],

            "buscas": buscas

        })

    return resultado
