import os
import requests
from buscador import executar_busca


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_mensagem(texto):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": texto
        }
    )


def main():

    resultados = executar_busca()

    mensagem = "🔎 Resultado da busca Cadeira360\n\n"

   if resultados:

    mensagem += "\n\n".join(resultados)

    else:

        mensagem += "Nenhum resultado encontrado."


    enviar_mensagem(mensagem)


if __name__ == "__main__":
    main()
