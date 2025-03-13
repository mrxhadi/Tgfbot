from telethon import events
from database import Database
from filters import process_message

db = Database()

@events.register(events.NewMessage)
async def forward_message(event):
    source_chat = event.chat_id
    dest_chat = db.get_channels().get(str(source_chat))

    print(f"[ℹ️] Current channels mapping: {db.get_channels()}")
    print(f"[✅] forward_message triggered from: {source_chat}")

    if not dest_chat:
        print(f"[❌] No destination found for source: {source_chat}")
        return

    text = event.raw_text if event.raw_text else None
    processed_text = process_message(text) if text else None

    # بررسی پیام‌های فقط متنی
    if event.media:
        if processed_text:
            print(f"[📤] Forwarding media with processed caption to {dest_chat}: {processed_text}")
            await event.client.send_message(int(dest_chat), processed_text, file=event.media)
        else:
            print(f"[📤] Forwarding media without caption to {dest_chat}")
            await event.client.send_file(int(dest_chat), event.media)
    else:
        if processed_text:
            print(f"[📤] Forwarding text to {dest_chat}: {processed_text}")
            await event.client.send_message(int(dest_chat), processed_text)
        else:
            print(f"[🚫] Message blocked by filters: {text}")
