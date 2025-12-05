from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

FLAG = "CTF{vazamento_natalino_sql}"
SECRET_TOKEN = "BPN-NATAL-ADMIN-94821"


def query_db(query, params=None):
    params = params or ()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            return cursor.execute(query, params).fetchall()
    except sqlite3.Error:
        return []


@app.route("/")
def index():
    # Página inicial com formulário de busca
    return render_template("index.html")


@app.route("/auditoria/search")
def search():
    campo = request.args.get("campo", "").strip()[:80]
    query = "SELECT descricao, valor FROM transacoes WHERE descricao LIKE ?"
    rows = query_db(query, (f"%{campo}%",))
    return render_template("search.html", rows=rows)


@app.route("/auditoria/validar")
def validar():
    token = request.args.get("token", "")
    if token == SECRET_TOKEN:
        return render_template("token.html", flag=FLAG, valido=True)
    return render_template("token.html", flag=None, valido=False)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})
