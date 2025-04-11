import requests

# Tvoj bot token i chat ID
bot_token = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"
chat_id = "7334208491"  # Tvoj lični Telegram ID
poruka = "👋 Zdravo Darko! Beba Srećko je sada online i čeka tvoje komande."

# Funkcija za slanje poruke
def posalji_poruku(poruka):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": poruka
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ Poruka uspešno poslata!")
    else:
        print(f"❌ Greška pri slanju! Kod: {response.status_code}")
        print(f"Detalji: {response.text}")

# Test poruka
posalji_poruku(poruka)


