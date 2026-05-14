# =========================
# BINANCE SETTINGS
# =========================
SYMBOLS = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    "SOL/USDT",
    "XRP/USDT",
    "DOGE/USDT",
    "ADA/USDT",
    "AVAX/USDT",
    "LINK/USDT",
    "LTC/USDT",
    "BCH/USDT",
    "DOT/USDT",
    "TRX/USDT",
    "MATIC/USDT",
    "TON/USDT",
    "ATOM/USDT",
    "APT/USDT",
    "ARB/USDT",
    "OP/USDT",
    "SUI/USDT",
    "WLD/USDT",
    "NEAR/USDT",
    "PEPE/USDT",
    "1000PEPE/USDT",
    "SHIB/USDT",
    "UNI/USDT",
    "ETC/USDT",
    "FIL/USDT",
    "INJ/USDT",
    "SEI/USDT"
]

TIMEFRAME = "1m"

WINDOW_SIZE = 50


# =========================
# PATTERN DETECTION
# =========================

ALERT_THRESHOLD = 75

WATCH_THRESHOLD = 68

PATTERN_FOLDER = "patterns"


# =========================
# TELEGRAM
# =========================

import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
