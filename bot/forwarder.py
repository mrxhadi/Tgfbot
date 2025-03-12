from telethon import events
from database import Database
from filters import process_message

db = Database()

@events.register(events.NewMessage(chats=list(db.get_channels().keys())))
async def forward_message(event):
    source_chat = event.chat_id
    dest_chat = db.get_channels().get(str(source_chat))

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
