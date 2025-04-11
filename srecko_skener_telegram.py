from binance.client import Client
import requests

# 🔐 Tvoj Binance API ključ i secret
API_KEY = "SreckoBot"
API_SECRET = "Zc52fqB5I7W33bk0uOUO7eI53kp2dI4Vg1DOGuN8jNTeYJ6iSWevieOBZfbuKYOJ"

# 🤖 Tvoj Telegram bot token i chat ID
BOT_TOKEN = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"
CHAT_ID = "7334208491"

# 📦 Inicijalizacija Binance klijenta
client = Client(API_KEY, API_SECRET)

def uzmi_top_parove():
    try:
        ticker = client.get_ticker()
        sortirani = sorted(ticker, key=lambda x: float(x['quoteVolume']), reverse=True)
        top10 = sortirani[:10]

        linije = ["📊 Top 10 najlikvidnijih parova po 24h volumenu:\n"]
        for par in top10:
            simbol = par['symbol']
            cena = par['lastPrice']
            volumen = par['quoteVolume']
            linije.append(f"{simbol}: Cena ${float(cena):,.2f} | Volumen ${float(volumen):,.2f}")

        return "\n".join(linije)

    except Exception as e:
        return f"⚠️ Greška prilikom preuzimanja sa Binance-a: {e}"

def posalji_telegram_poruku(poruka):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": poruka
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"❌ Telegram greška: {response.text}")
    except Exception as e:
        print(f"❌ Nije moguće poslati poruku na Telegram: {e}")

# 🚀 Glavna funkcija
if __name__ == "__main__":
    poruka = uzmi_top_parove()
    print(poruka)
    posalji_telegram_poruku(poruka)
