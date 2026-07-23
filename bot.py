from buscador import gerar_buscas

dados = gerar_buscas()

mensagem = "🔎 Resultado da busca Cadeira360\n\n"

for produto in dados:

    mensagem += f"🪑 {produto['produto']}\n\n"

    for busca in produto["buscas"]:

        mensagem += (
            f"📍 {busca['site']}\n"
            f"🔍 {busca['pesquisa']}\n"
            f"{busca['link']}\n\n"
        )

    mensagem += "-----------------------------\n\n"
