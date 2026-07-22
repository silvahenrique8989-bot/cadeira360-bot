import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Cadeira360 Bot iniciado!\n\n"
        "Comandos disponíveis:\n"
        "/orbital - procurar Safety 1st Orbital 360\n"
        "/inxt - procurar Safety 1st i-NXT"
    )


async def orbital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 Buscando Safety 1st Orbital 360...\n\n"
        "Primeira versão do monitoramento será ativada em breve."
    )


async def inxt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 Buscando Safety 1st i-NXT...\n\n"
        "Primeira versão do monitoramento será ativada em breve."
    )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("orbital", orbital))
    app.add_handler(CommandHandler("inxt", inxt))

    print("Bot rodando...")

    app.run_polling()


if __name__ == "__main__":
    main()
