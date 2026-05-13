import requests

TOKEN = "твой_токен"
CHAT_ID = "твой_chat_id"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": "🚀 Бот работает"
})
