import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    valor INTEGER,
    categoria TEXT,
    token_admin TEXT
)
""")

cursor.execute(
    "INSERT INTO transacoes (descricao, valor, categoria, token_admin) VALUES (?, ?, ?, ?)",
    ("Compra no Trenó Express", 150, "externo", None),
)

cursor.execute(
    "INSERT INTO transacoes (descricao, valor, categoria, token_admin) VALUES (?, ?, ?, ?)",
    ("Auditoria sobre o Motor de Transações Natalinas", 2000, "interno", None),
)

cursor.execute(
    "INSERT INTO transacoes (descricao, valor, categoria, token_admin) VALUES (?, ?, ?, ?)",
    ("Operação interna reservada", 9999, "administrativo", "BPN-NATAL-ADMIN-94821"),
)

conn.commit()
conn.close()

print("Banco inicializado com sucesso.")
