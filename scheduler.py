# email_scheduler.py
from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
import sqlite3
import datetime
import os


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS") or "your_email@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") or "your_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

DB_NAME = "emails.db"


app = Flask(__name__)
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS scheduled_emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        send_time TEXT NOT NULL,
        sent INTEGER DEFAULT 0
    )
''')
conn.commit()


@app.route("/schedule", methods=["POST"])
def schedule_email():
    """
    Accepts JSON: {"email":"recipient@example.com", "message":"Hello", "time":"YYYY-MM-DD HH:MM"}
    """
    data = request
