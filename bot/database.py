import os
import json

DATABASE_PATH = "database.json"

class Database:
    def __init__(self):
        self.data = {}  
        if os.path.exists(DATABASE_PATH):
            self._load_database()  
            print(f"[INFO] Database loaded: {self.data}")
        else:
            print("[WARNING] No database found. Waiting for database upload...")  

    def _load_database(self):
        with open(DATABASE_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def _save_database(self):
        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
        print("[INFO] Database saved!")

    def replace_database(self, new_data):
        print(f"[INFO] Replacing database with new data: {new_data}")
        self.data = new_data  
        print(f"[DEBUG] self.data after assignment: {self.data}")
        self._save_database()  
        self._load_database()  
        print(f"[INFO] Database successfully loaded into memory: {self.data}")

    def get_channels(self):
        print(f"[DEBUG] self.data before returning channels: {self.data}")  # لاگ مقدار کل دیتابیس
        channels = self.data.get("channels", {})
        print(f"[DEBUG] get_channels() returning: {channels}")  # لاگ مقدار کانال‌ها
        return channels

    def get_filters(self):
        return self.data.get("filters", {"remove_words": [], "replace_words": {}, "block_words": []})
