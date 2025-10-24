from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{loop_blocked_successfully}")
EXPECTED = "CTF{loop_blocked_successfully}"

TOPOLOGY = {
    "bridges": [
        {
            "name": "switch-ivy",
            "priority": 8192,
            "mac": "00:aa:bb:cc:dd:01",
            "ports": ["eth0", "eth1"],
        },
        {
            "name": "switch-nile",
            "priority": 8192,
            "mac": "00:aa:bb:cc:dd:10",
            "ports": ["eth0", "eth1"],
        },
    ],
    "links": [
        {"a": "switch-ivy:eth0", "b": "switch-nile:eth0"},
        {"a": "switch-ivy:eth1", "b": "switch-nile:eth1"},
    ],
}

PORT_STATES = [
    {
        "interface": "switch-ivy:eth0",
        "role": "root",
        "state": "forwarding",
        "cost": 4,
    },
    {
        "interface": "switch-ivy:eth1",
        "role": "alternate",
        "state": "blocking",
        "cost": 19,
    },
    {
        "interface": "switch-nile:eth0",
        "role": "designated",
        "state": "forwarding",
        "cost": 4,
    },
    {
        "interface": "switch-nile:eth1",
        "role": "designated",
        "state": "forwarding",
        "cost": 19,
    },
]

METRICS = {
    "switch-ivy:eth0": {"bpdu_rx": 12, "bpdu_tx": 18},
    "switch-ivy:eth1": {"bpdu_rx": 5, "bpdu_tx": 2},
    "switch-nile:eth0": {"bpdu_rx": 18, "bpdu_tx": 12},
    "switch-nile:eth1": {"bpdu_rx": 2, "bpdu_tx": 5},
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/topology")
def topology():
    return jsonify(TOPOLOGY)


@app.route("/states")
def states():
    return jsonify({"ports": PORT_STATES})


@app.route("/metrics")
def metrics():
    return jsonify(METRICS)


@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    flag = str(data.get("flag", "")).strip()
    if flag == EXPECTED:
        return jsonify({"flag": FLAG})
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
