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

# VALUTE I PRAGOVI (više nema dupliranja!)
valute = {
    "bitcoin": {"symbol": "BTC", "tip": ">", "granica": 90000},
    "ethereum": {"symbol": "ETH", "tip": ">", "granica": 3000},
    "solana": {"symbol": "SOL", "tip": ">", "granica": 200},
    "dogecoin": {"symbol": "DOGE", "tip": "<", "granica": 0.10},
    "shiba-inu": {"symbol": "SHIB", "tip": ">", "granica": 0.00001}
}

def dohvati_i_proveri():
    ids = ",".join(valute.keys())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)

    vreme = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    log = [f"\n[{vreme}] Pregled tržišta:"]

    if response.status_code == 200:
        data = response.json()
        for coin_id, info in valute.items():
            symbol = info["symbol"]
            cena = data[coin_id]["usd"]
            linija = f"- {symbol}: ${cena}"
            log.append(linija)
            print(linija)

            if info["tip"] == ">" and cena > info["granica"]:
                poruka = f"⚠️ {symbol} je IZNAD granice: ${cena}"
                posalji_poruku(poruka)
                log.append(poruka)

            elif info["tip"] == "<" and cena < info["granica"]:
                poruka = f"‼️ {symbol} je ISPOD granice: ${cena}"
                posalji_poruku(poruka)
                log.append(poruka)

    else:
        log.append("❌ Greska pri dohvatanju cena.")

    with open("srecko_log.txt", "a", encoding="utf-8") as f:
        for linija in log:
            f.write(linija + "\n")

# PETLJA
while True:
    dohvati_i_proveri()
    time.sleep(30)