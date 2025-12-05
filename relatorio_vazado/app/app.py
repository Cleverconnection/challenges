from flask import Flask, request, jsonify, render_template
import sqlite3, os

app = Flask(__name__,
            template_folder="templates",
            static_folder="static")

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

FLAG = "CTF{vazamento_natalino_sql}"
SECRET_TOKEN = "BPN-NATAL-ADMIN-94821"


def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        rows = cursor.execute(query).fetchall()
    except Exception:
        rows = []
    conn.close()
    return rows


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/suporte")
def suporte():
    return render_template("suporte.html")


@app.route("/auditoria/search")
def search():
    campo = request.args.get("campo", "")

    # SQLi proposital — LIKE aberto facilita UNION
    query = f"""
        SELECT descricao, valor
        FROM transacoes
        WHERE descricao LIKE '%{campo}'
    """

    rows = query_db(query)
    return render_template("search.html", rows=rows)


@app.route("/auditoria/validar")
def validar():
    token = request.args.get("token", "")
    if token == SECRET_TOKEN:
        return render_template("token.html", valido=True, flag=FLAG)
    return render_template("token.html", valido=False, flag=None)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})
