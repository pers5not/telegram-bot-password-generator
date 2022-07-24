import requests
from pprint import pprint

bot_token = ""
api_link = f"https://api.telegram.org/bot{bot_token}/"
updates = requests.get(api_link + "getUpdates?offset=-1").json()
pprint(updates)
message = updates["result"][0]["message"]
chat_id = message["from"]["id"]
text = message['caption']
print(text)

send_message = requests.get(
    api_link + f"sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")
