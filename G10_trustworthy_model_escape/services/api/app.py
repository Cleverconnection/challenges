import os
import uuid
import json
from pathlib import Path
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
WORKER_URL = os.environ.get("WORKER_URL", "http://localhost:5011")
STATUS_FILE = Path(os.environ.get("STATUS_FILE", "/tmp/status.json"))


def carregar_status():
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text())
    return {}


def salvar_status(dados):
    STATUS_FILE.write_text(json.dumps(dados, ensure_ascii=False, indent=2))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/painel")
def painel():
    return render_template("painel.html")


@app.route("/submeter", methods=["POST"])
def submeter():
    corpo = request.get_json(silent=True) or {}
    carga = {
        "id": str(uuid.uuid4()),
        "imagem": corpo.get("imagem", "desconhecida"),
        "metadados": corpo.get("metadados", {}),
        "mensagem_auditoria": corpo.get("mensagem_auditoria", "")
    }
    status = carregar_status()
    status[carga["id"]] = {"estado": "processando"}
    salvar_status(status)
    try:
        requests.post(f"{WORKER_URL}/processar", json=carga, timeout=5)
    except requests.RequestException:
        status[carga["id"]] = {"estado": "erro"}
        salvar_status(status)
        return jsonify({"erro": "Falha ao contatar worker"}), 502
    return jsonify({"id": carga["id"], "estado": "enfileirado"})


@app.route("/status/<identificador>")
def status(identificador):
    dados = carregar_status()
    return jsonify(dados.get(identificador, {"estado": "desconhecido"}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
