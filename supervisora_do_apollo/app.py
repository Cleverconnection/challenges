from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{Software_On_The_Moon}")
SECRET_PROGRAM = "PROG1201-OVERRIDE"

ALARMS = [
    {"code": 1201, "module": "LM guidance", "description": "Executive overflow preventivo"},
    {"code": 1202, "module": "LM guidance", "description": "Backup de navegação ativado"},
    {"code": 0, "module": "Checklist", "description": "Rotinas reiniciadas com sucesso"},
]

CHECKLIST = [
    "Verificar prioridade da fila de tarefas",
    "Reiniciar o integrador",
    "Confirmar PROG1201-OVERRIDE",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/alarms")
def alarms():
    return jsonify({"alarms": ALARMS})


@app.route("/checklist")
def checklist():
    return jsonify({"steps": CHECKLIST})


@app.route("/guidance")
def guidance():
    program = request.args.get("program", "").strip().upper()
    if program == SECRET_PROGRAM:
        return FLAG
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
