from telegram.ext import Updater, CommandHandler
import requests
from binance.client import Client

# Tvoj bot token i chat ID
BOT_TOKEN = "7961331230:AAFb88c2PQrQ-a06kFn1KqXa4SuXU9CweDM"
CHAT_ID = 7334208491

# Tvoj Binance API ključevi
BINANCE_API_KEY = "OVDE_UNESI_API_KEY"
BINANCE_API_SECRET = "OVDE_UNESI_SECRET"

# Komanda /start
def start(update, context):
    update.message.reply_text("👋 Zdravo Darko! Beba Srećko je sada online i čeka tvoje komande.")

# Komanda /cena
def cena(update, context):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        btc_price = response.json()["bpi"]["USD"]["rate"]
        update.message.reply_text(f"💰 BTC trenutno vredi: ${btc_price}")
    except Exception as e:
        update.message.reply_text(f"⚠️ Ne mogu da dohvatim cenu BTC-a.\nGreška: {e}")

# Komanda /pozdrav
def pozdrav(update, context):
    update.message.reply_text("⚡ Samo jako brate moj! Tržište je tvoje!")

# Komanda /status
def status(update, context):
    update.message.reply_text("📡 Srećko aktivan. Pratim BTC, ETH, DOGE, SHIB, SOL. Javljam kad bude vatre!")

# Komanda /skener
def skener(update, context):
    try:
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
        tickers = client.get_ticker()
        top = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)[:10]

        poruka = "\n📊 Top 10 najlikvidnijih parova po 24h volumenu:\n"
        for t in top:
            symbol = t['symbol']
            price = float(t['lastPrice'])
            volume = float(t['quoteVolume'])
            poruka += f"{symbol}: Cena ${price:,.2f}  |  Volumen ${volume:,.2f}\n"

        context.bot.send_message(chat_id=update.effective_chat.id, text=poruka)
    except Exception as e:
        update.message.reply_text(f"❌ Telegram greška: {e}")

# Glavna funkcija
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cena", cena))
    dp.add_handler(CommandHandler("pozdrav", pozdrav))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("skener", skener))

    print("✅ Beba Srećko bot je pokrenut!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
