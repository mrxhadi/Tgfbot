from telethon import events
from database import Database
from filters import process_message

db = Database()

@events.register(events.NewMessage(func=lambda e: e.is_channel and str(e.chat_id) in db.get_channels()))
async def forward_message(event):
    source_chat = event.chat_id
    dest_chat = db.get_channels().get(str(source_chat))

    # نادیده گرفتن پیام‌های فوروارد شده
    if event.fwd_from:
        print(f"[🚫] Ignoring forwarded message from: {source_chat}")
        return

    if not dest_chat:
        print(f"[❌] No destination found for source: {source_chat}")
        return

    text = event.raw_text
    print(f"[✅] Received message from {source_chat}: {text}")

    processed_text = process_message(text)

    if processed_text:
        print(f"[🔄] Forwarding to {dest_chat}: {processed_text}")
        await event.client.send_message(int(dest_chat), processed_text)
    else:
        print(f"[🚫] Message blocked by filters: {text}")
