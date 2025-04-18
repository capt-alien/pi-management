#!/usr/bin/env python3

from twilio.rest import Client
import os

# Read directly from environment (exported in ~/.bashrc)
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_from = os.environ["TWILIO_PHONE_NUMBER"]
twilio_to = os.environ["ALERT_PHONE_NUMBER"]

def send_alert(message):
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body=message,
        from_=twilio_from,
        to=twilio_to
    )
    print(f"✅ Alert sent! SID: {msg.sid}")

# Example test
if __name__ == "__main__":
    send_alert("🚨 Raspberry Pi alert: Test message!")
