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

INTERVAL = 60 * 15  # svakih 15 minuta
PROMENA_PRAG = 10.0  # % promena
BROJ_PAROVA = 5  # broj top skokova/padova koje šaljemo

poslednji_alert = {"gore": [], "dole": []}

def posalji(poruka):
    print(poruka)
    bot.send_message(chat_id=chat_id, text=poruka)

def proveri_top_movers():
    try:
        tickers = client.get_ticker()
        usdt_parovi = [t for t in tickers if t['symbol'].endswith('USDT') and float(t['quoteVolume']) > 1000000]

        sortirani_rast = sorted(usdt_parovi, key=lambda x: float(x['priceChangePercent']), reverse=True)
        sortirani_pad = sorted(usdt_parovi, key=lambda x: float(x['priceChangePercent']))

        poruka_rast = "\n🚀 Top 5 SKOKOVA (15min refresh):\n"
        novi_gore = []
        for t in sortirani_rast[:BROJ_PAROVA]:
            simbol = t['symbol']
            procenat = float(t['priceChangePercent'])
            if procenat >= PROMENA_PRAG:
                poruka_rast += f"{simbol}: +{procenat:.2f}%\n"
                novi_gore.append(simbol)

        if novi_gore and novi_gore != poslednji_alert['gore']:
            posalji(poruka_rast)
            poslednji_alert['gore'] = novi_gore

        poruka_pad = "\n🔻 Top 5 PADOVA (15min refresh):\n"
        novi_dole = []
        for t in sortirani_pad[:BROJ_PAROVA]:
            simbol = t['symbol']
            procenat = float(t['priceChangePercent'])
            if procenat <= -PROMENA_PRAG:
                poruka_pad += f"{simbol}: {procenat:.2f}%\n"
                novi_dole.append(simbol)

        if novi_dole and novi_dole != poslednji_alert['dole']:
            posalji(poruka_pad)
            poslednji_alert['dole'] = novi_dole

    except Exception as e:
        print(f"⚠️ Greška: {e}")

# Glavna petlja
while True:
    proveri_top_movers()
    time.sleep(INTERVAL)
