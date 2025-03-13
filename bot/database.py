import os
import json

DATABASE_PATH = "database.json"

class Database:
    def __init__(self):
        self.data = None  # مقدار اولیه None تا وقتی که دیتابیس دریافت شود
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
        print(f"[INFO] Replacing database with new data...")
        self.data = new_data.copy()  # اطمینان از این که مقدار جدید به درستی ذخیره شده
        self._save_database()
        self._load_database()
        print(f"[INFO] Database successfully loaded into memory: {self.data}")

    def get_channels(self):
        if self.data is None:
            print("[WARNING] Database is not loaded. Returning empty channels.")
            return {}
        channels = self.data.get("channels", {})
        print(f"[DEBUG] get_channels() returning: {channels}")
        return channels

    def get_filters(self):
        if self.data is None:
            print("[WARNING] Database is not loaded. Returning default filters.")
            return {"remove_words": [], "replace_words": {}, "block_words": []}
        return self.data.get("filters", {"remove_words": [], "replace_words": {}, "block_words": []})
