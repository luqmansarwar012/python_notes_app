from dotenv import load_dotenv
import smtplib
import os

load_dotenv()
email_host = os.getenv("EMAIL_HOST")
smtp_port = os.getenv("SMTP_PORT")
username = os.getenv("MAILMUG_USERNAME")
password = os.getenv("MAILMUG_PASSWORD")


def send_email(reciever_email: str, username: str):
    smtp_session = smtplib.SMTP(email_host, smtp_port)
    smtp_session.esmtp_features["auth"] = "LOGIN PLAIN"
    smtp_session.login(username, password)
    message = f"Hi {username}, Welcome to notes app."
    smtp_session.sendmail("luqmanrajput012@gmail.com", reciever_email, message)
    smtp_session.quit()
