from binance.client import Client
import telegram
import time

# Binance API podaci
api_key = "SreckoBot"
api_secret = "Zc52fqB5I7W33bk0uOUO7eI53kp2dI4Vg1DOGuN8jNTeYJ6iSWevieOBZfbuKYOJ"

# Telegram bot podaci
telegram_token = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"
chat_id = "7334208491"  # Tvoj chat ID

# Postavka
VOLUMEN_PRAG = 2_000_000_000  # 2 milijarde USDT
VREME_PROVERE = 60 * 30  # 30 minuta

client = Client(api_key, api_secret)
bot = telegram.Bot(token=telegram_token)

def proveri_volumen():
    print("🔁 Provera volumena...")
    try:
        tickers = client.get_ticker()
        for ticker in tickers:
            symbol = ticker['symbol']
            volumen = float(ticker['quoteVolume'])

            if volumen > VOLUMEN_PRAG and symbol.endswith("USDT"):
                poruka = f"🚨 Visok volumen: {symbol}\n📊 Volumen: ${volumen:,.2f}"
                bot.send_message(chat_id=chat_id, text=poruka)
                print(f"✅ Alert poslat za: {symbol}")
    except Exception as e:
        print(f"⚠️ Greška: {e}")

# Beskonačna petlja sa proverom na svakih 30 minuta
while True:
    proveri_volumen()
    time.sleep(VREME_PROVERE)