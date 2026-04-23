import subprocess
import time
import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT = os.getenv("CHAT_ID")

def notify(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": CHAT, "text": msg},
            timeout=5
        )
    except:
        pass

while True:
    print("🚀 Starting bot...")
    notify("🚀 Bot started")

    process = subprocess.Popen(["python", "bot.py"])

    while True:
        time.sleep(10)

        # check crash
        if process.poll() is not None:
            notify("❌ Bot crashed. Restarting...")
            break

        # check heartbeat
        if os.path.exists("heartbeat.txt"):
            with open("heartbeat.txt", "r") as f:
                last = float(f.read())

            if time.time() - last > 60:
                notify("⚠️ Bot frozen. Restarting...")
                process.kill()
                break

    time.sleep(5)