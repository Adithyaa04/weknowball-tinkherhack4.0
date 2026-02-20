import json
import os
from datetime import datetime

REMINDERS_FILE = "data/reminders.json"
os.makedirs("data", exist_ok=True)

def load_reminders():
    if not os.path.exists(REMINDERS_FILE):
        return {}
    with open(REMINDERS_FILE, "r") as f:
        return json.load(f)

def save_reminders(data):
    with open(REMINDERS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_today_str():
    return datetime.now().strftime("%Y-%m-%d")

def get_display_date(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return d.strftime("%A, %d %B %Y")

def get_today_reminders():
    data = load_reminders()
    return data.get(get_today_str(), [])

def get_past_reminders():
    data = load_reminders()
    today = get_today_str()
    past = {}
    for date_str, reminders in data.items():
        if date_str != today and reminders:
            past[date_str] = {
                "display": get_display_date(date_str),
                "reminders": reminders
            }
    # Sort newest first
    return dict(sorted(past.items(), reverse=True))

def add_reminder(text, time, icon):
    data = load_reminders()
    today = get_today_str()
    if today not in data:
        data[today] = []
    data[today].append({
        "id": str(datetime.now().timestamp()),
        "text": text,
        "time": time,
        "icon": icon,
        "done": False
    })
    save_reminders(data)

def toggle_reminder(reminder_id):
    data = load_reminders()
    today = get_today_str()
    for r in data.get(today, []):
        if r["id"] == reminder_id:
            r["done"] = not r["done"]
            break
    save_reminders(data)

def delete_reminder(reminder_id):
    data = load_reminders()
    today = get_today_str()
    data[today] = [r for r in data.get(today, []) if r["id"] != reminder_id]
    save_reminders(data)