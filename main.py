import os
from telegram import Bot
from time import sleep

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

def main():
    send_message("🤖 Supreme Bot attivo!")
    while True:
        send_message("🔄 Bot operativo...")
        sleep(300)

if __name__ == "__main__":
    main()
  
