"""
buscador.py

Gerencia todas as fontes de busca do Cadeira360.
"""


from fontes import mercadolivre



def buscar_ofertas(produto):
    """
    Consulta todas as fontes disponíveis
    e retorna uma lista de ofertas.
    """

    ofertas = []


    # Mercado Livre
    resultados_ml = mercadolivre.buscar(produto)

    ofertas.extend(resultados_ml)


    return ofertas
