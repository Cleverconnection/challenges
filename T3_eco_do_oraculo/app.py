import hashlib
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from flask import Response

app = Flask(__name__)
app.secret_key = "eco"
BASE = Path(__file__).resolve().parent
UPLOADS = BASE / "uploads"
REGISTRO = BASE / "registros" / "fluxo.log"

UPLOADS.mkdir(parents=True, exist_ok=True)
REGISTRO.parent.mkdir(parents=True, exist_ok=True)
FLAG = "CTF{Trinity_Log_Do_Oraculo}"

REGISTRO.write_text(
    (
        "Registro de envios da Oráculo\n"
        "Linha inicial criada por Trinity para lembrar Neo de ler as evidências.\n"
        f"Entrada fixa: {FLAG}\n\n"
    )
)


def salvar_registro(nome: str, tamanho: int, digest: str) -> None:
    linha = f"arquivo={nome};tamanho={tamanho};assinatura={digest}\n"
    REGISTRO.write_text(REGISTRO.read_text() + linha)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    arquivo = request.files.get("arquivo")
    if not arquivo or arquivo.filename == "":
        flash("Envie um arquivo válido.")
        return redirect(url_for("inicio"))

    destino = UPLOADS / arquivo.filename
    conteudo = arquivo.read()
    destino.write_bytes(conteudo)
    digest = hashlib.sha256(conteudo).hexdigest()
    salvar_registro(arquivo.filename, len(conteudo), digest)
    flash("Envio concluído. Consulte os registros para detalhes.")
    return redirect(url_for("inicio"))


@app.route("/registros")
def ver_registros():
    return Response(REGISTRO.read_text(), mimetype="text/plain")


@app.route("/arquivos/<nome>")
def ver_arquivo(nome):
    destino = UPLOADS / nome
    if destino.exists():
        return send_file(destino)
    return Response("Arquivo não encontrado", status=404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
