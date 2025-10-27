import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "CTF{fei_fei_memoria_azul}")

CENAS = {
    "luz_azul.png": {
        "titulo": "Laboratório iluminado",
        "descricao": "Um painel azul mostrando voluntárias rotulando imagens para o ImageNet.",
        "cor": "AZUL",
        "frase": "Imagens são histórias sobre pessoas.",
    },
    "floresta_verde.png": {
        "titulo": "Coleta colaborativa",
        "descricao": "Pesquisadores coletam imagens em um parque verdejante.",
        "cor": "VERDE",
        "frase": "Uma câmera nunca deve excluir pessoas da narrativa.",
    },
    "por_do_sol.png": {
        "titulo": "Cidade ao entardecer",
        "descricao": "A equipe analisa dados em um pôr do sol vermelho.",
        "cor": "VERMELHO",
        "frase": "Rotular bem é respeitar a diversidade de histórias.",
    },
}


@app.route("/")
def index():
    return render_template("index.html", cenas=CENAS)


@app.route("/galeria")
def galeria():
    return render_template("galeria.html", cenas=CENAS)


@app.route("/laboratorio")
def laboratorio():
    return render_template("laboratorio.html")


@app.route("/processar", methods=["POST"])
def processar():
    dados = request.get_json(silent=True) or {}
    nome = dados.get("imagem")
    cena = CENAS.get(nome)
    if not cena:
        return jsonify({"erro": "Imagem desconhecida"}), 404
    if cena["cor"] == "AZUL":
        return jsonify({"mensagem": cena["frase"], "flag": FLAG})
    return jsonify({"mensagem": cena["frase"], "flag": None})


@app.route("/saude")
def saude():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
