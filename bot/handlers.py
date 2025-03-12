from telethon import events
import os
import json
from database import Database

db = Database()
ADMIN_ID = int(os.getenv("ADMIN_ID"))

@events.register(events.NewMessage(pattern="^/list$"))
async def send_database(event):
    if event.sender_id != ADMIN_ID:
        print(f"[🚫] Unauthorized user tried to access /list: {event.sender_id}")
        return
    
    print(f"[📂] Sending database to admin: {event.sender_id}")
    await event.client.send_file(event.chat_id, "database.json", caption="Database file")

@events.register(events.NewMessage(incoming=True))
async def receive_database(event):
    if event.sender_id != ADMIN_ID:
        print(f"[🚫] Unauthorized user tried to send a database file: {event.sender_id}")
        return
    
    # پیام‌های معمولی را نادیده بگیر
    if not event.file:
        print(f"[🚫] Ignoring non-file message from admin: {event.sender_id}")
        return

    # بررسی اینکه فایل JSON هست یا نه
    if not event.file.name.endswith(".json"):
        print(f"[🚫] Ignoring non-JSON file from admin: {event.sender_id}")
        return

    # دریافت و جایگزینی دیتابیس
    file_path = await event.download_media("database.json")
    with open(file_path, "r", encoding="utf-8") as f:
        new_data = json.load(f)
        db.replace_database(new_data)

    print(f"[✅] Database updated by admin: {event.sender_id}")
    await event.reply("Database updated successfully.")
