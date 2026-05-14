import requests

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

LAST_UPDATE_ID = None


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


def check_telegram_commands():

    global LAST_UPDATE_ID

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"

    params = {}

    if LAST_UPDATE_ID is not None:
        params["offset"] = LAST_UPDATE_ID + 1

    try:

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if not data.get("ok"):
            return

        for update in data.get("result", []):

            LAST_UPDATE_ID = update["update_id"]

            message = update.get("message", {})
            text = message.get("text", "")
            chat_id = message.get("chat", {}).get("id")

            if text == "/start":

                requests.post(
                    f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": (
                            "✅ Market Eye AI Online\n\n"
                            "Scanner active.\n"
                            "Monitoring market patterns."
                        )
                    }
                )

            elif text == "/status":

                requests.post(
                    f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": (
                            "🟢 STATUS OK\n\n"
                            "Scanner running normally."
                        )
                    }
                )

    except Exception as e:
        print(f"Telegram command error: {e}")
