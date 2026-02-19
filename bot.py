from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")
MANAGER_ID = int(os.environ.get("MANAGER_ID"))

app = Flask(__name__)
print("ENV TOKEN =", repr(TOKEN))
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот працює 24/7 🚀")

application.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    import os

    TOKEN = os.environ.get("TOKEN")
    print("ENV TOKEN =", repr(TOKEN))

    application = ApplicationBuilder().token(TOKEN).build()

    application.run_polling()
