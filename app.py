from flask import Flask, render_template, request, redirect, url_for
from diary import add_entry, get_all_entries, delete_entry
from people import get_all_people, add_person, get_person, add_conversation, delete_person
from reminders import get_today_reminders, get_past_reminders, add_reminder, toggle_reminder, delete_reminder

app = Flask(__name__)

# ── DIARY ROUTES ──────────────────────────────────────────────

@app.route("/")
def home():
    entries = get_all_entries()
    return render_template("diary.html", entries=entries)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    text = request.form.get("text", "").strip()
    if text:
        add_entry(title or "My Entry", text)
    return redirect(url_for("home"))

@app.route("/delete/<int:entry_id>", methods=["POST"])
def delete(entry_id):
    delete_entry(entry_id)
    return redirect(url_for("home"))

# ── PEOPLE ROUTES ─────────────────────────────────────────────

@app.route("/people")
def people():
    return render_template("people.html", people=get_all_people())

@app.route("/people/add", methods=["POST"])
def add_person_route():
    name = request.form.get("name", "").strip()
    relation = request.form.get("relation", "").strip()
    tidbit = request.form.get("tidbit", "").strip()
    if name and relation:
        add_person(name, relation, tidbit)
    return redirect(url_for("people"))

@app.route("/people/<int:person_id>")
def person_profile(person_id):
    person = get_person(person_id)
    if not person:
        return redirect(url_for("people"))
    return render_template("person.html", person=person)

@app.route("/people/<int:person_id>/add_note", methods=["POST"])
def add_note(person_id):
    note = request.form.get("note", "").strip()
    if note:
        add_conversation(person_id, note)
    return redirect(url_for("person_profile", person_id=person_id))

@app.route("/people/delete/<int:person_id>", methods=["POST"])
def delete_person_route(person_id):
    delete_person(person_id)
    return redirect(url_for("people"))

# ── REMINDERS ROUTES ──────────────────────────────────────────

@app.route("/reminders")
def reminders():
    return render_template("reminders.html",
                           today=get_today_reminders(),
                           past=get_past_reminders())

@app.route("/reminders/add", methods=["POST"])
def add_reminder_route():
    text = request.form.get("text", "").strip()
    time = request.form.get("time", "").strip()
    icon = request.form.get("icon", "🔔").strip()
    if text:
        add_reminder(text, time, icon)
    return redirect(url_for("reminders"))

@app.route("/reminders/toggle/<reminder_id>", methods=["POST"])
def toggle_reminder_route(reminder_id):
    toggle_reminder(reminder_id)
    return redirect(url_for("reminders"))

@app.route("/reminders/delete/<reminder_id>", methods=["POST"])
def delete_reminder_route(reminder_id):
    delete_reminder(reminder_id)
    return redirect(url_for("reminders"))

if __name__ == "__main__":
    app.run(debug=True)