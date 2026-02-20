from flask import Flask, render_template, request, redirect, url_for, jsonify
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from diary import add_entry, get_all_entries, delete_entry

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)