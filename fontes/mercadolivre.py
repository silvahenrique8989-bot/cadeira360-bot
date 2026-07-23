"""
mercadolivre.py

Busca ofertas no Mercado Livre.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote



def buscar(produto):
    """
    Busca produtos no Mercado Livre
    e retorna ofertas encontradas.
    """

    ofertas = []

    nome_produto = produto["nome"]

    busca = quote(nome_produto)

    url = (
        "https://lista.mercadolivre.com.br/"
        f"{busca}"
    )


    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64)"
        )
    }


    try:

        resposta = requests.get(
            url,
            headers=headers,
            timeout=20
        )


        if resposta.status_code != 200:

            print(
                f"Mercado Livre erro HTTP: {resposta.status_code}"
            )

            return ofertas


        soup = BeautifulSoup(
            resposta.text,
            "lxml"
        )


        produtos = soup.select(
            "li.ui-search-layout__item"
        )


        for item in produtos[:5]:

            titulo = item.select_one(
                "h2"
            )


            preco = item.select_one(
                "span.andes-money-amount__fraction"
            )


            link = item.select_one(
                "a"
            )


            if not titulo or not preco or not link:
                continue


            valor = preco.text.replace(".", "")


            try:

                valor = float(valor)

            except:

                continue



            ofertas.append(
                {
                    "loja": "Mercado Livre",
                    "preco": valor,
                    "link": link.get("href")
                }
            )


        print(
            f"Mercado Livre: {len(ofertas)} ofertas encontradas."
        )


    except Exception as erro:

        print(
            f"Erro Mercado Livre: {erro}"
        )


    return ofertas
