from binance.client import Client
import telegram
import time

# Binance i Telegram podaci
api_key = "SreckoBot"
api_secret = "Zc52fqB5I7W33bk0uOUO7eI53kp2dI4Vg1DOGuN8jNTeYJ6iSWevieOBZfbuKYOJ"
telegram_token = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"
chat_id = "7334208491"

client = Client(api_key, api_secret)
bot = telegram.Bot(token=telegram_token)

# Postavke za 3 valute koje pratiš
valute = {
    "BTCUSDT": {"gore": 85000, "dole": 80000, "volumen": 2_000_000_000},
    "ETHUSDT": {"gore": 4000, "dole": 3000, "volumen": 1_000_000_000},
    "SOLUSDT": {"gore": 150, "dole": 100, "volumen": 500_000_000},
}

INTERVAL = 60 * 5  # na svakih 5 minuta

def posalji(poruka):
    print(poruka)
    bot.send_message(chat_id=chat_id, text=poruka)

def proveri():
    try:
        tickers = client.get_ticker()
        for t in tickers:
            simbol = t['symbol']
            if simbol in valute:
                cena = float(t['lastPrice'])
                volumen = float(t['quoteVolume'])
                granice = valute[simbol]

                # Price alert
                if cena > granice['gore']:
                    posalji(f"🚀 {simbol} PREŠAO ${granice['gore']:,}! Cena: ${cena:,.2f}")
                elif cena < granice['dole']:
                    posalji(f"🔻 {simbol} PAO ispod ${granice['dole']:,}! Cena: ${cena:,.2f}")

                # Volume alert
                if volumen > granice['volumen']:
                    posalji(f"📊 Ogroman volumen na {simbol}!\nVolumen: ${volumen:,.2f}")

    except Exception as e:
        print(f"⚠️ Greška: {e}")

while True:
    proveri()
    time.sleep(INTERVAL)