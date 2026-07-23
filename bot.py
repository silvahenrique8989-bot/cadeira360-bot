"""
bot.py

Controla o fluxo principal do Cadeira360.
"""

import json

from config import PRODUTOS_FILE
from buscador import buscar_ofertas
from telegram import enviar_mensagem
from historico import ultimo_preco, atualizar


def carregar_produtos():
    """
    Carrega os produtos monitorados.
    """

    with open(PRODUTOS_FILE, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["produtos"]


def executar():
    """
    Executa o monitor.
    """

    produtos = carregar_produtos()

    for produto in produtos:

        if not produto.get("ativo", True):
            continue

        print(f"Verificando: {produto['nome']}")

        ofertas = buscar_ofertas(produto)

        for oferta in ofertas:

            ultimo = ultimo_preco(
                produto["nome"],
                oferta["loja"]
            )

            if ultimo == oferta["preco"]:
                print(
                    f"Preço repetido em {oferta['loja']}. Ignorado."
                )
                continue

            mensagem = f"""
🪑 {produto['nome']}

🏪 {oferta['loja']}

💰 R$ {oferta['preco']:.2f}

🔗 {oferta['link']}
"""

            enviado = enviar_mensagem(mensagem.strip())

            if enviado:
                atualizar(
                    produto["nome"],
                    oferta["loja"],
                    oferta["preco"],
                    oferta["link"]
                )
