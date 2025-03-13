from database import Database
import re

db = Database()

def process_message(text: str) -> str | None:
    filters = db.get_filters()

    for word in filters["block_words"]:
        if re.search(rf'\b{re.escape(word)}\b', text, flags=re.IGNORECASE):
            return None

    for word in filters["remove_words"]:
        text = re.sub(rf'\b{re.escape(word)}\b', '', text, flags=re.IGNORECASE)

    for old_word, new_word in filters["replace_words"].items():
        text = re.sub(rf'\b{re.escape(old_word)}\b', new_word, text, flags=re.IGNORECASE)

    return text.strip() if text.strip() else None
