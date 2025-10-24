from flask import Flask, jsonify, render_template, send_file, abort, request
import os
from pathlib import Path

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{falsa_root_00:11:22:33:44:99}")
EXPECTED = "CTF{falsa_root_00:11:22:33:44:99}"

TRACE_PATH = Path(__file__).parent / "static" / "tree_guard_trace.txt"

ANALYSIS = {
    "legitimate_root": "00:11:22:33:44:55",
    "designated_bridge": "00:11:22:33:44:66",
    "suspicious_root": "00:11:22:33:44:99",
    "explanation": "Root ID igual ao MAC do emissor indica tentativa de assumir controle.",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/trace")
def trace():
    if not TRACE_PATH.exists():
        abort(404)
    return send_file(TRACE_PATH, as_attachment=True)


@app.route("/analysis")
def analysis():
    return jsonify(ANALYSIS)


@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    flag = str(data.get("flag", "")).strip()
    if flag == EXPECTED:
        return jsonify({"flag": FLAG})
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
