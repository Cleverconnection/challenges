from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{Flowmatic_Debug_Master}")
SECRET_OPCODE = "FLOW-MATIC"

CONSOLE_LOG = [
    "MARK I INITIALIZATION COMPLETE",
    "TAPE A: F - Floating routine loaded",
    "TAPE B: L - Loop unrolled",
    "TAPE C: O - Operator patch applied",
    "TAPE D: W - Overflow trap armed",
    "TAPE E: M - Memory map stabilized",
    "TAPE F: A - Accumulator recalibrated",
    "TAPE G: T - Transfer vector updated",
    "TAPE H: I - Interrupts synchronized",
    "TAPE I: C - Card reader cleared",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/console")
def console():
    return jsonify({"log": CONSOLE_LOG})


@app.route("/punchcard")
def punchcard():
    opcode = request.args.get("opcode", "").strip().upper()
    if opcode == SECRET_OPCODE:
        return FLAG
    abort(418)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
