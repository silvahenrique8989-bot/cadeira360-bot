import json
import os

ARQUIVO = "data/historico.json"


def carregar_historico():

    if not os.path.exists(ARQUIVO):
        return {}

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)



def salvar_historico(dados):

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )



def ultimo_preco(produto, loja):

    historico = carregar_historico()

    try:
        return historico[produto][loja]["preco"]

    except KeyError:
        return None



def atualizar(produto, loja, preco, link):

    historico = carregar_historico()


    if produto not in historico:
        historico[produto] = {}


    historico[produto][loja] = {
        "preco": preco,
        "link": link
    }


    salvar_historico(historico)
