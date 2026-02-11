
from api import fetch_prices
from config import COINS, CURRENCY

def main():
    print("🚀 Krypto-Dashboard gestartet\n")
    
    prices = fetch_prices(COINS, CURRENCY)

    if not prices:
        print("❌ Keine Daten verfügbar.")
        return
    
    print("📊 Aktuelle Kurse:\n")

    for coin in COINS:
        value = prices.get(coin, {}).get(CURRENCY)

        if value is None:
            print(f"{coin.capitalize()}: ❌ keine Daten")
        else:
            print(f"{coin.capitalize():<10}: {value:,.2f} {CURRENCY.upper()}")


if __name__ == "__main__":
    main()


