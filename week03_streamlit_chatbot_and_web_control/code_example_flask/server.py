from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# This list lives in memory on the server.
# Every time someone POSTs to /log, we add a new entry here.
logs = []


@app.route("/", methods=["GET"])
def home():
    # Simple check to see if server is alive.
    return "✅ Cloud Flask Server is running"


@app.route("/log", methods=["POST"])
def log_data():
    """
    This is the main endpoint students will use to log data.

    Expected JSON example:
    {
        "group_id": 1,
        "project": "fall_detection",
        "value": 0.95,
        "note": "no fall detected"
    }
    """
    data = request.get_json() or {}

    entry = {
        "id": len(logs) + 1,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "group_id": data.get("group_id"),
        "project": data.get("project"),
        "value": data.get("value"),
        "note": data.get("note"),
        "raw": data,  # store full payload just in case
    }

    logs.append(entry)
    print("New entry:", entry)

    return jsonify({"status": "ok", "entry": entry}), 201


@app.route("/log", methods=["GET"])
def get_all_logs():
    # Return *all* entries from all groups and projects.
    return jsonify(logs)


@app.route("/log/<int:group_id>", methods=["GET"])
def get_group_logs(group_id):
    # Filter only entries that match this group_id.
    filtered = [e for e in logs if e.get("group_id") == group_id]
    return jsonify(filtered)


if __name__ == "__main__":
    # Local testing only. In the cloud we use gunicorn instead.
    app.run(host="0.0.0.0", port=5000, debug=True)
