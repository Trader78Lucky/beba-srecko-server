import requests

BOT_TOKEN = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    try:
        chat_id = data["result"][-1]["message"]["chat"]["id"]
        print(f"Tvoj chat ID je: {chat_id}")
    except (IndexError, KeyError):
        print("Pošalji poruku botu na Telegramu (/start) pa ponovo pokreni skriptu.")
else:
    print(f"Greška pri dohvatanju podataka: {response.status_code}")
