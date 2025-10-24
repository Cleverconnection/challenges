from flask import Flask, jsonify, render_template, request, abort, send_file
import os
from pathlib import Path

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{Arvores_Digitais_Seguras}")

TOPOLOGY = [
    {
        "name": "switch-alpha",
        "priority": 4096,
        "mac": "00:11:22:33:44:55",
        "uplinks": ["switch-beta", "switch-delta"],
    },
    {
        "name": "switch-beta",
        "priority": 8192,
        "mac": "00:11:22:AA:BB:CC",
        "uplinks": ["switch-alpha", "switch-gamma"],
    },
    {
        "name": "switch-gamma",
        "priority": 8192,
        "mac": "00:AA:BB:CC:DD:EE",
        "uplinks": ["switch-beta"],
    },
    {
        "name": "switch-delta",
        "priority": 4096,
        "mac": "00:11:22:33:44:99",
        "uplinks": ["switch-alpha"],
    },
]


def compute_root_bridge():
    root = min(TOPOLOGY, key=lambda node: (node["priority"], node["mac"]))
    return f"{root['priority']}.{root['mac']}"


ROOT_BRIDGE_ID = compute_root_bridge()


@app.route("/")
def index():
    return render_template("index.html", root_bridge=ROOT_BRIDGE_ID)


@app.route("/health")
def health():
    return "OK", 200


@app.route("/topology")
def topology():
    return jsonify({"nodes": TOPOLOGY})


@app.route("/bridge/<name>")
def bridge(name: str):
    for node in TOPOLOGY:
        if node["name"] == name:
            return jsonify(node)
    abort(404)


@app.route("/flag")
def flag():
    candidate = request.headers.get("X-Root-Bridge", "").strip()
    if candidate == ROOT_BRIDGE_ID:
        return FLAG
    abort(403)


@app.route("/pcap-script")
def pcap_script():
    script_path = Path(__file__).parent / "static" / "generate_root_bridge_pcap.py"
    if not script_path.exists():
        abort(404)
    return send_file(script_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
