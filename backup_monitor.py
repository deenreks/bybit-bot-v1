import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT = os.getenv("CHAT_ID")

HEALTH_URL = "http://178.104.86.127:5000/health"

def send(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": CHAT, "text": msg},
            timeout=5
        )
    except:
        pass

alerting = False
send("🟢 Backup monitor started")
while True:
    try:
        r = requests.get(HEALTH_URL, timeout=5)

        if r.status_code != 200:
            send("🚨 MAIN VPS DOWN!")
            alerting = True

        else:
            if alerting:
                send("✅ MAIN VPS RECOVERED")
            alerting = False

    except:
        send("🚨 VPS NOT REACHABLE!")

    time.sleep(30)

