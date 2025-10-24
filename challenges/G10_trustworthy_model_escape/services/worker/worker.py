import os
import json
from pathlib import Path
import requests

VALIDATOR_URL = os.environ.get("VALIDATOR_URL", "http://localhost:5012")
STATUS_FILE = Path(os.environ.get("STATUS_FILE", "/tmp/status.json"))


def carregar_status():
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text())
    return {}


def salvar_status(dados):
    STATUS_FILE.write_text(json.dumps(dados, ensure_ascii=False, indent=2))


def processar_carga(carga):
    status = carregar_status()
    identificador = carga.get("id")
    try:
        resposta = requests.post(f"{VALIDATOR_URL}/validar", json=carga, timeout=5)
        status[identificador] = resposta.json()
    except requests.RequestException:
        status[identificador] = {"estado": "erro"}
    salvar_status(status)


if __name__ == "__main__":
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    @app.route("/processar", methods=["POST"])
    def processar_endpoint():
        carga = request.get_json(silent=True) or {}
        processar_carga(carga)
        return jsonify({"status": "processado"})

    app.run(host="0.0.0.0", port=5011)
