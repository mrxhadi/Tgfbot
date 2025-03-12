import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from handlers import send_database, receive_database
from forwarder import forward_message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

client.add_event_handler(send_database)
client.add_event_handler(receive_database)
client.add_event_handler(forward_message)

if __name__ == "__main__":
    print("Bot is running...")
    client.start()
    client.run_until_disconnected()
