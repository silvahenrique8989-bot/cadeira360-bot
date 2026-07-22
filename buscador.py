import json
import urllib.parse


def carregar_produtos():

    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def criar_links(produto):

    termo = urllib.parse.quote(produto["busca"])

    resultados = []

    resultados.append(
        f"🪑 {produto['nome']}\n"
    )

    resultados.append(
        "Amazon:\n"
        f"https://www.amazon.com.br/s?k={termo}\n"
    )

    resultados.append(
        "Mercado Livre:\n"
        f"https://lista.mercadolivre.com.br/{termo}\n"
    )

    resultados.append(
        "Google Shopping:\n"
        f"https://www.google.com/search?tbm=shop&q={termo}\n"
    )

    resultados.append(
        "------------------------"
    )

    return "\n".join(resultados)


def executar_busca():

    produtos = carregar_produtos()

    mensagens = []

    for produto in produtos:

        mensagens.append(
            criar_links(produto)
        )

    return mensagens
