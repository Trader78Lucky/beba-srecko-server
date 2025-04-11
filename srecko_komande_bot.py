from telegram.ext import Updater, CommandHandler
from binance.client import Client
import os

# Tvoj API i SECRET ključ sa Binance
BINANCE_API_KEY = "SreckoBot"
BINANCE_SECRET_KEY = "Zc52fqB5I7W33bk0uOUO7eI53kp2dI4Vg1DOGuN8jNTeYJ6iSWevieOBZfbuKYOJ"

# Tvoj BOT token i chat ID
BOT_TOKEN = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"
CHAT_ID = "7334208491"

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

# Funkcija za komandu /skener
def skener(update, context):
    try:
        tickers = client.get_ticker()
        top_parovi = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)[:10]

        poruka = "\U0001F50D Top 10 najlikvidnijih parova po 24h volumenu:\n"
        for par in top_parovi:
            simbol = par['symbol']
            cena = par['lastPrice']
            volumen = float(par['quoteVolume'])
            poruka += f"{simbol}: Cena ${cena} | Volumen ${volumen:,.2f}\n"

        context.bot.send_message(chat_id=CHAT_ID, text=poruka)
    except Exception as e:
        context.bot.send_message(chat_id=CHAT_ID, text=f"❌ Greska: {e}")

# Funkcija za /start i ostale komande
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="👋 Zdravo Darko! Beba Srećko je sada online i čeka tvoje komande.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("skener", skener))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
