import json
import os
from datetime import datetime

DIARY_FILE = "data/diary.json"

os.makedirs("data", exist_ok=True)

def load_entries():
    if not os.path.exists(DIARY_FILE):
        return []
    with open(DIARY_FILE, "r") as f:
        return json.load(f)

def save_entries(entries):
    with open(DIARY_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def add_entry(title, text):
    entries = load_entries()
    new_entry = {
        "id": len(entries) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "display_date": datetime.now().strftime("%A, %d %B %Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "title": title,
        "text": text
    }
    entries.insert(0, new_entry)  # newest first
    save_entries(entries)
    return new_entry

def delete_entry(entry_id):
    entries = load_entries()
    entries = [e for e in entries if e["id"] != entry_id]
    save_entries(entries)

def get_all_entries():
    return load_entries()