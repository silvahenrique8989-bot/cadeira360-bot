import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": texto,
            "parse_mode": "HTML"
        }
    )

def main():
    mensagem = (
        "✅ Bot Cadeira360 está funcionando!\n\n"
        "Em breve ele começará a pesquisar promoções automaticamente."
    )

    enviar_mensagem(mensagem)

if __name__ == "__main__":
    main()
