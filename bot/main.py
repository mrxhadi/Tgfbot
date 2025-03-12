import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from handlers import send_database, receive_database
from forwarder import forward_message
from database import Database

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

db = Database()

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

client.add_event_handler(send_database)
client.add_event_handler(receive_database)
client.add_event_handler(forward_message)

print("Bot is running... Monitoring channels:", db.get_channels().keys())

# اضافه کردن لاگ فقط برای پیام‌های جدید (نه آپدیت‌های وضعیت کاربر)
def log_event(event_name, event):
    if isinstance(event, events.NewMessage.Event):
        print(f"[✅] Event Triggered: {event_name} | Chat ID: {event.chat_id}")

@events.register(events.NewMessage)
async def send_database_with_log(event):
    log_event("send_database", event)
    await send_database(event)

@events.register(events.NewMessage)
async def receive_database_with_log(event):
    log_event("receive_database", event)
    await receive_database(event)

@events.register(events.NewMessage)
async def forward_message_with_log(event):
    log_event("forward_message", event)
    await forward_message(event)

client.add_event_handler(send_database_with_log)
client.add_event_handler(receive_database_with_log)
client.add_event_handler(forward_message_with_log)

if __name__ == "__main__":
    client.start()
    print("Bot started successfully and is listening for messages...")
    client.run_until_disconnected()
