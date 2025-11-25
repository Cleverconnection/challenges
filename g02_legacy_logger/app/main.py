from __future__ import annotations

from flask import Flask, render_template, request, redirect, url_for, flash
import codecs
from pathlib import Path

app = Flask(__name__)
app.secret_key = "laboratorio_lilas"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def processar_log(conteudo: str) -> list[str]:
    linhas_processadas: list[str] = []
    for linha in conteudo.splitlines():
        if linha.startswith("mensagem:"):
            prefixo, texto = linha.split(":", 1)
            traduzido = codecs.decode(texto.strip(), "rot13")
            linhas_processadas.append(f"{prefixo}: {traduzido}")
        else:
            linhas_processadas.append(linha)
    return linhas_processadas


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.get("/linha-do-tempo")
def linha_do_tempo() -> str:
    return render_template("timeline.html")


@app.get("/laboratorio")
def laboratorio() -> str:
    conteudo_exemplo = (DATA_DIR / "registro_legacy.txt").read_text(encoding="utf-8")
    linhas = processar_log(conteudo_exemplo)
    return render_template("lab.html", linhas=linhas)


@app.post("/upload")
def upload() -> str:
    arquivo = request.files.get("arquivo")
    if not arquivo:
        flash("Envie um arquivo válido, cadete!", "erro")
        return redirect(url_for("index"))

    conteudo = arquivo.read().decode("utf-8", errors="ignore")
    linhas = processar_log(conteudo)
    flash("Arquivo traduzido com sucesso. Veja o resultado abaixo!", "sucesso")
    return render_template("resultado.html", linhas=linhas)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=False)
