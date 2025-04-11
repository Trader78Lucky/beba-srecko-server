from binance.client import Client

# 🔐 Ubaci svoje Binance API ključeve ovde
API_KEY = "SreckoBot"
API_SECRET = "Zc52fqB5I7W33bk0uOUO7eI53kp2dI4Vg1DOGuN8jNTeYJ6iSWevieOBZfbuKYOJ"

client = Client(API_KEY, API_SECRET)

# 📊 Funkcija koja prikazuje top 10 najtrgovanijih parova
def prikazi_top_10_parova():
    try:
        tickers = client.get_ticker_24hr()
        sortirano = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)
        
        print("📈 Top 10 najlikvidnijih parova po 24h volumenu:")
        for ticker in sortirano[:10]:
            simbol = ticker['symbol']
            cena = ticker['lastPrice']
            volumen = ticker['quoteVolume']
            print(f"{simbol}: Cena ${cena} | Volumen ${volumen}")
    
    except Exception as e:
        print(f"⚠️ Greška prilikom dohvatanja podataka: {e}")

# 🔁 Pokreni skener
if __name__ == '__main__':
    prikazi_top_10_parova()

