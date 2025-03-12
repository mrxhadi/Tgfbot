import os
from telethon import TelegramClient
from handlers import send_database, receive_database
from forwarder import forward_message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=STRING_SESSION)

client.add_event_handler(send_database)
client.add_event_handler(receive_database)
client.add_event_handler(forward_message)

if __name__ == "__main__":
    print("Bot is running...")
    client.run_until_disconnected()
