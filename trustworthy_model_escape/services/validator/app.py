import os
import json
from pathlib import Path
from flask import Flask, request, jsonify

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "CTF{fei_fei_pipeline_escape}")
STATUS_FILE = Path(os.environ.get("STATUS_FILE", "/tmp/status.json"))


def carregar_status():
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text())
    return {}


def salvar_status(dados):
    STATUS_FILE.write_text(json.dumps(dados, ensure_ascii=False, indent=2))


@app.route("/validar", methods=["POST"])
def validar():
    carga = request.get_json(silent=True) or {}
    identificador = carga.get("id")
    auditoria = carga.get("mensagem_auditoria", "")
    resultado = {"estado": "validado", "flag": None}
    if "LIBERAR_FLAG" in auditoria:
        resultado["flag"] = FLAG
    status = carregar_status()
    status[identificador] = resultado
    salvar_status(status)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
