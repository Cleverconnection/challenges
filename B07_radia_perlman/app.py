from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CECYBER{root_change_detected}")
EXPECTED = "CECYBER{root_change_detected}"

LAB = {
    "bridges": [
        {
            "name": "switch-alpha",
            "priority": 4096,
            "mac": "00:11:22:33:44:55",
            "ports": ["eth0", "eth1"],
        },
        {
            "name": "switch-orion",
            "priority": 4096,
            "mac": "00:11:22:33:44:41",
            "ports": ["eth0", "eth1"],
        },
    ],
    "links": [
        {"a": "switch-alpha:eth0", "b": "switch-orion:eth0"},
        {"a": "switch-alpha:eth1", "b": "switch-orion:eth1"},
    ],
}

TIMELINE = [
    {
        "timestamp": 0.0,
        "emitter": "switch-alpha",
        "detail": "Initial root announcement priority=4096 mac=00:11:22:33:44:55",
    },
    {
        "timestamp": 6.2,
        "emitter": "switch-orion",
        "detail": "Receives BPDU, recalculates cost via eth1",
    },
    {
        "timestamp": 12.5,
        "emitter": "switch-orion",
        "detail": "Root takeover priority=4096 mac=00:11:22:33:44:41",
    },
    {
        "timestamp": 13.0,
        "emitter": "switch-alpha",
        "detail": "Marks port eth1 as blocking",
    },
    {
        "timestamp": 15.4,
        "emitter": "switch-orion",
        "detail": "Confirms new root and forwards only on eth0",
    },
]

HINTS = [
    "Prioridade é comparada antes do MAC; empates são decididos pelo endereço.",
    "Quando um BPDU anuncia um MAC menor com mesma prioridade, ocorre troca de raiz.",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/lab")
def lab():
    return jsonify(LAB)


@app.route("/timeline")
def timeline():
    return jsonify({"events": TIMELINE})


@app.route("/hints")
def hints():
    return jsonify({"hints": HINTS})


@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    flag = str(data.get("flag", "")).strip()
    if flag == EXPECTED:
        return jsonify({"flag": FLAG})
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
