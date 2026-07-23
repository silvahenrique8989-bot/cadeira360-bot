"""
historico.py

Responsável por ler e salvar o histórico de preços enviados.
"""

import json
from pathlib import Path

from config import HISTORICO_FILE


def carregar():
    """
    Carrega o histórico.
    """

    if not Path(HISTORICO_FILE).exists():
        return {}

    try:
        with open(HISTORICO_FILE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except Exception:
        return {}


def salvar(historico):
    """
    Salva o histórico.
    """

    with open(HISTORICO_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(
            historico,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def ultimo_preco(produto, loja):
    """
    Retorna o último preço salvo.
    """

    historico = carregar()

    return (
        historico
        .get(produto, {})
        .get(loja, {})
        .get("preco")
    )


def atualizar(produto, loja, preco, link):
    """
    Atualiza o histórico.
    """

    historico = carregar()

    if produto not in historico:
        historico[produto] = {}

    historico[produto][loja] = {
        "preco": preco,
        "link": link
    }

    salvar(historico)
