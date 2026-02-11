
import requests
from config import API_URL, TIMEOUT


def fetch_prices(coins, currency):
    params = {
        "ids": ",".join(coins),
            "vs_currencies": currency
    }

    try:
        response = requests.get(API_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout:
        print("⏱️ Timeout - API nicht erreichbar")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"🚫 HTTP Fehler: {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Netzwerkfehler: {e}")
        return None
    


    