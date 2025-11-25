from pathlib import Path
from flask import Flask, render_template, send_from_directory, abort, request, Response

app = Flask(__name__)
BASE = Path(__file__).resolve().parent
PUBLICO = BASE / "memorias_publicas"
USUARIO = "trinity"
SENHA = "c0d3_liberta_zion"
FLAG = "CTF{Trinity_Zion_SSH}"


@app.route("/")
def inicio():
    arquivos = sorted(p.name for p in PUBLICO.iterdir())
    return render_template("index.html", arquivos=arquivos)


@app.route("/memorias/<nome>")
def memorias(nome):
    try:
        return send_from_directory(PUBLICO, nome)
    except FileNotFoundError:
        abort(404)


@app.route("/listagem")
def listagem():
    conteudo = "\n".join(sorted(p.name for p in PUBLICO.iterdir()))
    return Response(conteudo + "\n", mimetype="text/plain")


@app.route("/ssh")
def ssh():
    auth = request.authorization
    if not auth or auth.username != USUARIO or auth.password != SENHA:
        resposta = Response("Credenciais rejeitadas pela porta 22 de Zion", status=401)
        resposta.headers["WWW-Authenticate"] = "Basic realm=Zion"
        return resposta
    return Response(
        "Bem-vindo a Zion, aliado. Flag: {flag}\n".format(flag=FLAG),
        mimetype="text/plain",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)
