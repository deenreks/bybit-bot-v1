from flask import Flask, request

app = Flask(__name__)

active_owner = None

@app.route("/lock", methods=["POST"])
def lock():
    global active_owner
    requester = request.json.get("id")

    if active_owner is None:
        active_owner = requester
        return {"status": "granted"}
    elif active_owner == requester:
        return {"status": "already_owner"}
    else:
        return {"status": "denied", "owner": active_owner}

@app.route("/release", methods=["POST"])
def release():
    global active_owner
    requester = request.json.get("id")

    if active_owner == requester:
        active_owner = None
        return {"status": "released"}

    return {"status": "not_owner"}

app.run(host="0.0.0.0", port=6000)