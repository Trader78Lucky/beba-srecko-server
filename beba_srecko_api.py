import requests

BOT_TOKEN = "7961331230:AAFb88c2PQrQ-a06kFn1KqXa4SuXU9CweDM"
CHAT_ID = "7334208491"

def posalji_poruku(poruka):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": poruka
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Poruka uspešno poslata!")
    else:
        print(f"❌ Greška pri slanju! Kod: {response.status_code}")
        print(f"Detalji: {response.text}")

# TEST poruka
posalji_poruku("Srećko javlja: Sistem je povezan sa Telegramom!")




