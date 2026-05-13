import requests

TOKEN = "8842150672:AAEvIdUGvOOyV_EGaCm5lFlOoklDiQk9_2I"
CHAT_ID = "453232276"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": "🚀 Бот работает"
})

print(response.status_code)
print(response.text)
