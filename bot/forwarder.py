from telethon import events
from database import Database
from filters import process_message

db = Database()

@events.register(events.NewMessage)
async def forward_message(event):
    source_chat = str(event.chat_id)
    dest_chat = db.get_channels().get(source_chat)

    if not dest_chat:
        return

    text_only_channels = db.get_text_only_channels()
    text = event.raw_text if event.raw_text else None
    processed_text = process_message(text) if text else None

    if source_chat in text_only_channels:
        if event.media and not text:
            return
        if processed_text:
            await event.client.send_message(int(dest_chat), processed_text)
    else:
        if event.media:
            if processed_text:
                await event.client.send_message(int(dest_chat), processed_text, file=event.media)
            else:
                await event.client.send_file(int(dest_chat), event.media)
        else:
            if processed_text:
                await event.client.send_message(int(dest_chat), processed_text)
