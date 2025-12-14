import requests
from config import BINANCE_BASE_URL

def get_price(symbol="BTCUSDT"):
    """
    يرجع آخر سعر لزوج معين من Binance
    """
    url = f"{BINANCE_BASE_URL}/api/v3/ticker/price"
    params = {"symbol": symbol}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return float(data["price"])
