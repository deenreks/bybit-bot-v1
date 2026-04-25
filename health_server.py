from flask import Flask
import time

app = Flask(__name__)

last_heartbeat = time.time()

@app.route("/health")
def health():
    if time.time() - last_heartbeat < 60:
        return "OK", 200
    return "DEAD", 500

@app.route("/heartbeat")
def heartbeat():
    global last_heartbeat
    last_heartbeat = time.time()
    return "updated", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)