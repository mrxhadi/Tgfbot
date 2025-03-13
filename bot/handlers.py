from telethon import events
import os
import json
from database import Database

db = Database()
ADMIN_ID = int(os.getenv("ADMIN_ID"))

@events.register(events.NewMessage)
async def handle_admin_commands(event):
    if event.sender_id != ADMIN_ID:
        return  # نادیده گرفتن پیام‌های غیر ادمین

    # بررسی ارسال دستور `/list`
    message_text = event.raw_text.strip()
    if message_text == "/list":
        await event.client.send_file(event.chat_id, "database.json", caption="Database file")
        return

    # بررسی ارسال فایل دیتابیس
    if event.file and event.file.name.endswith(".json"):
        file_path = await event.download_media("database.json")
        with open(file_path, "r", encoding="utf-8") as f:
            new_data = json.load(f)
            print(f"[📥] Received database: {new_data}")
            db.replace_database(new_data)  # جایگزینی دیتابیس جدید

        await event.reply("✅ Database updated successfully.")
