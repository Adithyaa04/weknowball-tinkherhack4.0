import json
import os
from datetime import datetime

PEOPLE_FILE = "data/people.json"
os.makedirs("data", exist_ok=True)

def load_people():
    if not os.path.exists(PEOPLE_FILE):
        return []
    with open(PEOPLE_FILE, "r") as f:
        return json.load(f)

def save_people(people):
    with open(PEOPLE_FILE, "w") as f:
        json.dump(people, f, indent=2)

def get_all_people():
    return load_people()

def get_person(person_id):
    people = load_people()
    for p in people:
        if p["id"] == person_id:
            return p
    return None

def add_person(name, relation, tidbit):
    people = load_people()
    new_person = {
        "id": len(people) + 1,
        "name": name,
        "relation": relation,
        "tidbit": tidbit,
        "last_visit": None,
        "conversations": []
    }
    people.append(new_person)
    save_people(people)
    return new_person

def add_conversation(person_id, note):
    people = load_people()
    for p in people:
        if p["id"] == person_id:
            p["conversations"].insert(0, {
                "note": note,
                "date": datetime.now().strftime("%A, %d %B %Y"),
                "time": datetime.now().strftime("%I:%M %p")
            })
            p["last_visit"] = datetime.now().strftime("%A, %d %B %Y")
            break
    save_people(people)

def delete_person(person_id):
    people = load_people()
    people = [p for p in people if p["id"] != person_id]
    save_people(people)