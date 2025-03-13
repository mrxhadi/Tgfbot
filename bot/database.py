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
        self.data = new_data
        self._save_database()
        self._load_database()
        
    def get_channels(self):
        return self.data.get("channels", {})

    def get_filters(self):
        return self.data.get("filters", {})
