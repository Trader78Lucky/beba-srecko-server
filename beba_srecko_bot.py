from telegram.ext import Updater, CommandHandler
import requests

BOT_TOKEN = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"

def start(update, context):
    update.message.reply_text("👋 Zdravo Darko! Beba Srećko je sada online i čeka tvoje komande.")

def cena(update, context):
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        btc_price = response.json()["bitcoin"]["usd"]
        update.message.reply_text(f"💰 BTC trenutno vredi: ${btc_price}")
    except Exception as e:
        update.message.reply_text(f"⚠️ Ne mogu da dohvatim cenu BTC-a.\nGreška: {e}")

def pozdrav(update, context):
    update.message.reply_text("⚡ Samo jako brate moj! Tržište je tvoje!")

def status(update, context):
    update.message.reply_text("📡 Srećko aktivan. Pratim BTC, ETH, DOGE, SHIB, SOL. Javljam kad bude vatre!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cena", cena))
    dp.add_handler(CommandHandler("pozdrav", pozdrav))
    dp.add_handler(CommandHandler("status", status))

    print("✅ Beba Srećko je pokrenut!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

