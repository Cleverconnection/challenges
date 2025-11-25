from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "CTF{Seeing_The_Unseen}")
SECRET_TAG = "IMAGENET-2009"

DATASET = [
    {
        "segment": 1,
        "keywords": ["IMA", "GE"],
        "description": "Cenas anotadas com apoio do laboratório de visão da Stanford.",
    },
    {
        "segment": 2,
        "keywords": ["NET", "-2009"],
        "description": "Lembre-se do ano em que o ImageNet foi oficialmente lançado para a comunidade.",
    },
    {
        "segment": 3,
        "keywords": ["1k classes", "milhões de imagens"],
        "description": "O projeto em larga escala deu origem ao boom do deep learning.",
    },
]

ANNOTATIONS = {
    "drone": ["vision", "dataset", "crowd"],
    "robot": ["learning", "features"],
    "atlas": ["semantics", "labels"],
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/dataset")
def dataset():
    return jsonify({"clips": DATASET})


@app.route("/annotations")
def annotations():
    return jsonify(ANNOTATIONS)


@app.route("/vision", methods=["POST"])
def vision():
    body = request.get_json(silent=True) or {}
    tags = body.get("tags", [])
    if not isinstance(tags, list):
        abort(400)
    normalized = [str(tag).strip().upper() for tag in tags]
    if SECRET_TAG in normalized:
        return jsonify({"flag": FLAG})
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
