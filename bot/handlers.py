from telethon import events
import json
import os
from database import Database

db = Database()

@events.register(events.NewMessage(pattern="/list"))
async def send_database(event):
    if event.sender_id == int(os.getenv("ADMIN_ID")):
        await event.client.send_file(event.chat_id, "database.json", caption="Database file")

@events.register(events.NewMessage(incoming=True))
async def receive_database(event):
    if event.sender_id == int(os.getenv("ADMIN_ID")) and event.file:
        if event.file.name.endswith(".json"):
            file_path = await event.download_media("database.json")
            with open(file_path, "r", encoding="utf-8") as f:
                new_data = json.load(f)
                db.replace_database(new_data)

            print("Database updated! Monitoring channels:", db.get_channels().keys())

            await event.reply("Database updated successfully.")
