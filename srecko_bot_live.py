import requests
import time
from datetime import datetime

# TELEGRAM KONFIG
BOT_TOKEN = "7961331230:AAFb88c2PQrQ-a06kFn1KqXa4SuXU9CweDM"
CHAT_ID = "7334208491"

def posalji_poruku(poruka):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": poruka}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"❌ Ne mogu da pošaljem poruku: {e}")

# CILJANE VALUTE I PRAGOVI
valute = {
    "bitcoin": {"symbol": "BTC", "upozorenje": 90000},
    "ethereum": {"symbol": "ETH", "upozorenje": 3000},
    "dogecoin": {"symbol": "DOGE", "upozorenje": 0.10},
    "shiba-inu": {"symbol": "SHIB", "upozorenje": 0.00001},
    "solana": {"symbol": "SOL", "upozorenje": 200},
}

def dohvati_i_proveri():
    ids = ",".join(valute.keys())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)

    vreme = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    log = [f"\n[{vreme}] Cene na tržištu:"]

    if response.status_code == 200:
        data = response.json()
        for coin_id, info in valute.items():
            cena = data[coin_id]["usd"]
            symbol = info["symbol"]
            linija = f"- {symbol}: ${cena}"
            print(linija)
            log.append(linija)

            if (symbol == "DOGE" and cena < info["upozorenje"]) or \
               (symbol != "DOGE" and cena > info["upozorenje"]):
                poruka = f"⚠️ {symbol} ALERT! Cena: ${cena}"
                posalji_poruku(poruka)
                log.append(poruka)
    else:
        log.append("❌ Greska u dohvatanju podataka sa CoinGecko.")

    with open("srecko_log.txt", "a", encoding="utf-8") as f:
        for linija in log:
            f.write(linija + "\n")

# Glavna petlja
while True:
    dohvati_i_proveri()
    time.sleep(30)