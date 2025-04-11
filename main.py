from flask import Flask, request
import telegram

# Tvoj bot token i chat ID
BOT_TOKEN = "7961331230:AAFb88c2PorQ-aO6KFnHkqXa4SuXu9CweDM"
CHAT_ID = "73345208491"

bot = telegram.Bot(token=BOT_TOKEN)

pp = Flask(__name__)

@app.route('/')
def index():
    return 'Beba Srećko server aktivan!'

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    message = data.get('message', 'Nema poruke.')
    try:
        bot.send_message(chat_id=CHAT_ID, text=f"🔥 TradingView ALERT:\n{message}")
        return 'Poruka poslata!', 200
    except Exception as e:
        return f"Greška: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)