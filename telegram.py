"""
telegram.py

Responsável pelo envio de mensagens ao Telegram.
"""

import requests

from config import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN


def enviar_mensagem(texto):
    """
    Envia uma mensagem para o Telegram.
    """

    if not TELEGRAM_TOKEN:
        print("Token do Telegram não configurado.")
        return False

    if not TELEGRAM_CHAT_ID:
        print("Chat ID do Telegram não configurado.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    dados = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "disable_web_page_preview": False
    }

    try:
        resposta = requests.post(url, data=dados, timeout=20)

        if resposta.status_code == 200:
            print("Mensagem enviada com sucesso.")
            return True

        print(f"Erro Telegram: {resposta.text}")
        return False

    except Exception as erro:
        print(f"Erro ao enviar mensagem: {erro}")
        return False
