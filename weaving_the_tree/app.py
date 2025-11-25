from flask import Flask, jsonify, render_template, send_file, abort, request
import os
from pathlib import Path

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "FLAG{root_32768_001122334466}")
EXPECTED_FLAG = "CECYBER{root_32768_001122334466}"

BPDU_EVENTS = [
    {
        "bridge_id": "32768.00:11:22:33:44:55",
        "role": "root",
        "cost": 0,
        "port_id": "0x8000",
        "note": "Estado inicial antes do enlace redundante entrar em operação.",
    },
    {
        "bridge_id": "32768.00:11:22:33:44:66",
        "role": "root",
        "cost": 4,
        "port_id": "0x8001",
        "note": "Bridge secundária anuncia menor MAC e força bloqueio da porta 1.",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/bpdu")
def bpdu():
    return jsonify({"events": BPDU_EVENTS})


@app.route("/pcap-script")
def pcap_script():
    script_path = Path(__file__).parent / "static" / "generate_weaving_pcap.py"
    if not script_path.exists():
        abort(404)
    return send_file(script_path, as_attachment=True)


@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    flag = str(data.get("flag", "")).strip()
    if flag == EXPECTED_FLAG:
        return jsonify({"flag": FLAG})
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
