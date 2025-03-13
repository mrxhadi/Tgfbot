import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from handlers import handle_admin_commands
from forwarder import forward_message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

client.add_event_handler(handle_admin_commands)  # اصلاح‌شده
client.add_event_handler(forward_message)

if __name__ == "__main__":
    client.start()
    print("[ℹ️] Bot is running and waiting for messages...")
    client.run_until_disconnected()
