import os
import json

DATABASE_PATH = "database.json"

DEFAULT_DATABASE = {
    "channels": {},
    "filters": {
        "remove_words": [],
        "replace_words": {},
        "block_words": []
    }
}

class Database:
    def __init__(self):
        self._load_database()
        print(f"[🔄] Database loaded: {self.data}")

    def _load_database(self):
        if os.path.exists(DATABASE_PATH):
            with open(DATABASE_PATH, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = DEFAULT_DATABASE
            self._save_database()

    def _save_database(self):
        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
        print("[💾] Database saved!")

    def replace_database(self, new_data):
        print(f"[🔄] Replacing database with new data: {new_data}")  # لاگ مقدار جدید
    
        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)
    
        print("[💾] Database saved!")
    
        self._load_database()
        print(f"[✅] Database successfully loaded into memory: {self.data}")
        
    def get_channels(self):
        if not hasattr(self, 'data'):
        print("[⚠️] Warning: self.data is not set. Reloading database...")
        self._load_database()
    
    channels = self.data.get("channels", {})
    print(f"[🔍] Updated get_channels() returning: {channels}")
    return channels

    def get_filters(self):
        return self.data.get("filters", {})
