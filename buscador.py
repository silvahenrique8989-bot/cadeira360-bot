import json
import urllib.parse


def carregar_produtos():

    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def criar_links(produto):

    termo = urllib.parse.quote(produto["busca"])

    mensagem = (
        f"🪑 {produto['nome']}\n\n"
        f"Amazon:\n"
        f"https://www.amazon.com.br/s?k={termo}\n\n"
        f"Mercado Livre:\n"
        f"https://lista.mercadolivre.com.br/{termo}\n\n"
        f"Google Shopping:\n"
        f"https://www.google.com/search?tbm=shop&q={termo}\n\n"
        f"------------------------"
    )

    return mensagem


def executar_busca():

    produtos = carregar_produtos()

    resultados = []

    for produto in produtos:

        resultados.append(
            criar_links(produto)
        )

    return resultados
