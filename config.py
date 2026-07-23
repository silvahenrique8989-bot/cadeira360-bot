"""
config.py

Centraliza todas as configurações do projeto.
"""

from pathlib import Path
import os

# ==========================
# Versão
# ==========================

VERSAO = "2.0.0"

# ==========================
# Diretórios
# ==========================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

PRODUTOS_FILE = DATA_DIR / "produtos.json"
HISTORICO_FILE = DATA_DIR / "historico.json"

# ==========================
# Telegram
# ==========================

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# ==========================
# Configurações Gerais
# ==========================

TIMEOUT = 20

LOG_ATIVADO = True

# ==========================
# Emojis
# ==========================

EMOJI_EXCELENTE = "🎉"
EMOJI_BOA = "🟡"
EMOJI_ERRO = "❌"
EMOJI_INFO = "ℹ️"
