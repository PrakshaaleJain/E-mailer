# 📧 Email Scheduler Microservice

A lightweight backend microservice built with **Flask**, **SQLite**, and **APScheduler** to schedule and send emails at a specified future time.  
The service provides a REST API endpoint to queue emails, stores them in a database, and automatically sends pending emails every minute via **SMTP**.

---

## 🚀 Features
- **REST API** to schedule emails (`POST /schedule`).
- **SQLite database** for persistence of scheduled tasks.
- **Background job scheduler** running every minute to send due emails.
- **SMTP integration** (works with Gmail, Outlook, and other providers).
- Simple & minimal — perfect for quick deployment.

---

## 🛠 Tech Stack
- **Python 3.8+**
- [Flask](https://flask.palletsprojects.com/)
- [APScheduler](https://apscheduler.readthedocs.io/)
- SQLite (built-in with Python)
- `smtplib` (Python standard library)

---

## 📂 Project Structure
