import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "CTF{fei_fei_phash_match}")

CATALOGO = {
    "arquivo_lab.png": "f3a5c791e2d48bc1",
    "inaauguracao_imagenet.png": "abcdef1234567890",
    "painel_anotacao.png": "9876cba543210fed",
}

MENSAGEM = {
    "arquivo_lab.png": "Cenas do laboratório de visão em Stanford.",
    "inaauguracao_imagenet.png": "Foto da inauguração do ImageNet em 2009.",
    "painel_anotacao.png": "Painel destacando rotuladores voluntários.",
}


def hamming(a, b):
    bits_a = bin(int(a, 16))[2:].zfill(64)
    bits_b = bin(int(b, 16))[2:].zfill(64)
    return sum(x != y for x, y in zip(bits_a, bits_b))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/catalogo")
def catalogo():
    itens = [
        {"nome": nome, "phash": phash, "descricao": MENSAGEM.get(nome)}
        for nome, phash in CATALOGO.items()
    ]
    return jsonify({"imagens": itens})


@app.route("/comparar", methods=["POST"])
def comparar():
    dados = request.get_json(silent=True) or {}
    phash = dados.get("phash")
    if not phash:
        return jsonify({"erro": "Informe um pHash"}), 400
    distancias = []
    for nome, ref in CATALOGO.items():
        distancias.append({
            "nome": nome,
            "distancia": hamming(phash, ref),
            "descricao": MENSAGEM.get(nome),
        })
    melhor = min(distancias, key=lambda x: x["distancia"])
    resposta = {"resultado": melhor}
    if melhor["nome"] == "inaauguracao_imagenet.png" and melhor["distancia"] == 0:
        resposta["flag"] = FLAG
    return jsonify(resposta)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
