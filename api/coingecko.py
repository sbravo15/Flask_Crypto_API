import requests
from api.cache import cache  # Import cache

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

@cache.memoize(timeout=300)  # Now cache should work properly
def fetch_crypto_data(coin: str, days: int):
    """Fetch historical price data from CoinGecko."""
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily'
    }
    response = requests.get(COINGECKO_URL.format(coin=coin), params=params)
    if response.status_code == 200:
        return response.json()
    return None
