import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BINANCE_BASE_URL = os.getenv("BINANCE_BASE_URL", "https://api.binance.com"/)
