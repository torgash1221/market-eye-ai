import requests

TOKEN = "8842150672:AAEvIdUGvOOyV_EGaCm5lFlOoklDiQk9_2I"
CHAT_ID = "453232276"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": "🚀 Бот работает"
})
