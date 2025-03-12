from database import Database

db = Database()

def process_message(text: str) -> str | None:
    filters = db.get_filters()

    
    for word in filters["block_words"]:
        if word in text:
            return None

    
    for word in filters["remove_words"]:
        text = text.replace(word, "")

    
    for old_word, new_word in filters["replace_words"].items():
        text = text.replace(old_word, new_word)

    return text.strip() if text.strip() else None
