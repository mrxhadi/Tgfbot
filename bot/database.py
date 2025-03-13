import os
import json

DATABASE_PATH = "database.json"

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.data = None
            if os.path.exists(DATABASE_PATH):
                cls._instance._load_database()
                print(f"[INFO] Database loaded: {cls._instance.data}")
            else:
                print("[WARNING] No database found. Waiting for database upload...")
        return cls._instance

    def _load_database(self):
        with open(DATABASE_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def _save_database(self):
        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
        print("[INFO] Database saved!")

    def replace_database(self, new_data):
        print(f"[INFO] Replacing database with new data...")
        self.data = new_data.copy()
        self._save_database()
        self._load_database()
        print(f"[INFO] Database successfully loaded into memory: {self.data}")

    def get_channels(self):
        if self.data is None:
            print("[WARNING] Database is not loaded. Returning empty channels.")
            return {}
        return self.data.get("channels", {})

    def get_text_only_channels(self):
        if self.data is None:
            print("[WARNING] Database is not loaded. Returning empty text-only channels.")
            return []
        return self.data.get("text_only_channels", [])

    def get_filters(self):
        if self.data is None:
            print("[WARNING] Database is not loaded. Returning default filters.")
            return {"remove_words": [], "replace_words": {}, "block_words": []}
        return self.data.get("filters", {"remove_words": [], "replace_words": {}, "block_words": []})
