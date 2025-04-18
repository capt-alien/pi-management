#!/usr/bin/env python3

import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ["ALERT_EMAIL_FROM"]
EMAIL_PASSWORD = os.environ["ALERT_EMAIL_PASS"]
EMAIL_TO = os.environ["ALERT_EMAIL_TO"]

def send_email_alert(subject, body, priority="INFO"):
    priority_map = {
        "INFO": "🔵 INFO",
        "WARNING": "🟠 WARNING",
        "CRITICAL": "🔴 CRITICAL"
    }

    prefix = priority_map.get(priority.upper(), "🔵 INFO")
    full_subject = f"{prefix} - {subject}"

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_TO
    msg["Subject"] = full_subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f"📧 {priority.upper()} alert sent!")

# Example usage
if __name__ == "__main__":
    send_email_alert(
        subject="Disk usage exceeded 90% on rp2",
        body="Node rp2 is at 93% disk usage on /dev/root.",
        priority="CRITICAL"
    )
