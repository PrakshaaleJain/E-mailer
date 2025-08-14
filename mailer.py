import smtplib
import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # server.ehlo()       # helps identify ourselves in gmail's logs
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Test Email"
    body = "This is a test email sent from Python!"

    message = f"Subject: {subject}\n\n{body}"
