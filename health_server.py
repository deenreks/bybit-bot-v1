from flask import Flask, request
import time

app = Flask(__name__)

heartbeats = {}  # store per bot

TIMEOUT = 30


@app.route("/health/<bot_name>")
def health(bot_name):
    last = heartbeats.get(bot_name)

    if last and time.time() - last < TIMEOUT:
        return "OK", 200

    return "DEAD", 500


@app.route("/heartbeat/<bot_name>")
def heartbeat(bot_name):
    heartbeats[bot_name] = time.time()
    return "updated", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)