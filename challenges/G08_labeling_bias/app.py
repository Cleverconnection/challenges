import json
import os
from pathlib import Path
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "CTF{fei_fei_bias_ajustado}")
DATASET_PATH = Path(__file__).parent / "data" / "dataset.json"


def carregar_registros():
    with open(DATASET_PATH, "r", encoding="utf-8") as fp:
        return json.load(fp)


def salvar_registros(registros):
    with open(DATASET_PATH, "w", encoding="utf-8") as fp:
        json.dump(registros, fp, ensure_ascii=False, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sessoes")
def sessoes():
    return render_template("sessoes.html")


@app.route("/avaliacao")
def avaliacao():
    return render_template("avaliacao.html")


@app.route("/dados")
def dados():
    return jsonify({"registros": carregar_registros()})


@app.route("/corrigir", methods=["POST"])
def corrigir():
    entrada = request.get_json(silent=True) or {}
    registros = entrada.get("registros")
    if not isinstance(registros, list):
        return jsonify({"erro": "Formato inválido"}), 400
    ajustes = 0
    for registro in registros:
        if registro.get("tom_de_pele") == "escuro":
            if registro.get("atributo") != "respeitado":
                return jsonify({"erro": "Viés não corrigido"}), 422
            ajustes += 1
    salvar_registros(registros)
    if ajustes > 0:
        return jsonify({"mensagem": "Viés corrigido", "flag": FLAG})
    return jsonify({"mensagem": "Nada alterado"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008)
