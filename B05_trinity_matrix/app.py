from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{Banco_de_Dados_da_Receita}")
ANSWER = "BANCO_DE_DADOS_DA_RECEITA"

HINTS = [
    "Revise a cena inicial no clube em Matrix (1999).",
    "Neo acreditava que Trinity era o hacker que invadiu um banco de dados governamental.",
    "Trinity confirma que derrubou o firewall da Receita Federal.",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/hints")
def hints():
    return jsonify({"hints": HINTS})


@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    answer = str(data.get("answer", "")).strip().upper().replace(" ", "_")
    if answer == ANSWER:
        return jsonify({"flag": FLAG})
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
