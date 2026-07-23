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



def analisar_oferta(produto, oferta):
    """
    Classifica a oferta conforme o preço alvo.
    """

    preco = oferta["preco"]
    alvo = produto["preco_alvo"]


    if preco <= 1500:

        percentual = ((alvo - preco) / alvo) * 100

        return {
            "status": "excelente",
            "mensagem": (
                "🎉 EXCELENTE OPORTUNIDADE\n\n"
                f"🪑 {produto['nome']}\n\n"
                f"🏪 {oferta['loja']}\n\n"
                f"💰 R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                f"📉 {percentual:.1f}% abaixo do seu preço-alvo\n\n"
                f"🔗 {oferta['link']}"
            )
        }


    elif preco <= 1700:

        percentual = ((preco - alvo) / alvo) * 100

        return {
            "status": "boa",
            "mensagem": (
                "🟡 BOA OFERTA\n\n"
                f"🪑 {produto['nome']}\n\n"
                f"🏪 {oferta['loja']}\n\n"
                f"💰 R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                f"📈 {percentual:.1f}% acima do seu preço-alvo\n\n"
                f"🔗 {oferta['link']}"
            )
        }


    else:

        return {
            "status": "ignorar",
            "mensagem": None
        }



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


            analise = analisar_oferta(produto, oferta)


            if analise["status"] == "ignorar":

                print(
                    f"Oferta ignorada: R$ {oferta['preco']}"
                )

                continue



            ultimo = ultimo_preco(
                produto["nome"],
                oferta["loja"]
            )


            if ultimo is not None and oferta["preco"] >= ultimo:

                print(
                    "Preço igual ou maior que o último enviado."
                )

                continue



            enviado = enviar_mensagem(
                analise["mensagem"]
            )


            if enviado:

                atualizar(
                    produto["nome"],
                    oferta["loja"],
                    oferta["preco"],
                    oferta["link"]
                )



if __name__ == "__main__":
    executar()
