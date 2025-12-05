from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

FLAG = "CTF{vazamento_natalino_sql}"
SECRET_TOKEN = "BPN-NATAL-ADMIN-94821"

def query_db(query, params=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        rows = cursor.execute(query, params or []).fetchall()
    except Exception:
        rows = []
    conn.close()
    return rows

@app.route("/")
def index():
    return """
    <h2>Painel de Auditoria - Banco Polar Nacional</h2>
    <p>Use o parâmetro <code>?campo=</code> para buscar registros.</p>
    <p>Exemplo: <code>/auditoria/search?campo=trenó</code></p>
    """

@app.route("/auditoria/search")
def search():
    campo = request.args.get("campo", "")
    query = "SELECT descricao, valor FROM transacoes WHERE descricao LIKE ?"
    rows = query_db(query, [f"%{campo}%"])

    html = "<h3>Resultados do Relatório:</h3><ul>"
    for r in rows:
        html += f"<li>{r[0]} — R${r[1]}</li>"
    html += "</ul>"

    return html

@app.route("/auditoria/validar")
def validar():
    token = request.args.get("token", "")
    if token == SECRET_TOKEN:
        return f"Flag: {FLAG}"
    return "Token inválido."

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
