import requests

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_telegram_message(message):

    if not TELEGRAM_BOT_TOKEN:
        print("Telegram token not set")
        return

    if not TELEGRAM_CHAT_ID:
        print("Telegram chat id not set")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)

    return response.json()
