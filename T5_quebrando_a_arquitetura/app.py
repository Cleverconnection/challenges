import hashlib
import hmac
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash, Response

app = Flask(__name__)
app.secret_key = "trinity"
BASE = Path(__file__).resolve().parent
PAGINAS = BASE / "templates" / "pages"
LOG = BASE / "logs" / "eco.log"
SEGREDO = BASE / "segredos" / "chave.txt"
FRASE = "ACESSO_ZION"
FLAG = "CTF{Trinity_Arquitetura_Liberada}"

LOG.parent.mkdir(parents=True, exist_ok=True)
SEGREDO.parent.mkdir(parents=True, exist_ok=True)

SEGREDO.write_text("m0rf3u5_compartilha\n")

if not LOG.exists():
    LOG.write_text(
        "Painel de auditoria — Trinity\n"
        "O último registro válido deve conter CHAVE=... gerado com SHA256 sobre a frase ACESSO_ZION.\n"
        "Valor atual inválido.\n"
    )


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/painel")
def painel():
    pagina = request.args.get("pagina", "boas_vindas.html")
    caminho = PAGINAS / pagina
    if not caminho.exists():
        flash("Página não encontrada.")
        return redirect(url_for("inicio"))
    conteudo = caminho.read_text(encoding="utf-8")
    return render_template("painel.html", conteudo=conteudo, pagina=pagina)


@app.route("/registrar")
def registrar():
    entrada = request.args.get("entrada", "")
    if not entrada:
        return Response("Informe uma entrada", status=400)
    atual = LOG.read_text()
    LOG.write_text(atual + entrada.strip() + "\n")
    return Response("Registro salvo\n", mimetype="text/plain")


@app.route("/flag")
def flag():
    linhas = LOG.read_text().strip().splitlines()
    if not linhas:
        return Response("Sem registros", status=403)
    ultimo = linhas[-1].strip()
    segredo = SEGREDO.read_text().strip()
    esperado = hmac.new(segredo.encode(), FRASE.encode(), hashlib.sha256).hexdigest()
    if ultimo == f"CHAVE={esperado}":
        return Response(f"Flag: {FLAG}\n", mimetype="text/plain")
    return Response("Registro final inválido", status=403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8084)
