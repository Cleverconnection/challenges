from pathlib import Path
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)
BASE = Path(__file__).resolve().parent
DIRETORIO_PUBLICO = BASE / "armazenamento"
FLAG = "CTF{Trinity_Pilula_Listagem}"

# arquivos disponíveis
(DIRETORIO_PUBLICO / "diario_trinity.txt").write_text(
    """Registro vermelho\n\nNeo, você quer saber o que é a Matrix? Escolha a pílula vermelha e acompanhe os erros de indexação.\n\n"""
    "Os operadores esqueceram de esconder nossos relatos.\n\n"
    "Flag: " + FLAG + "\n"
)
(DIRETORIO_PUBLICO / "roteiro_operacao.txt").write_text(
    "Ponto de encontro: Hotel Lafayette.\nVerificar cabos de fibra."
)


@app.route("/")
def inicio():
    arquivos = sorted(p.name for p in DIRETORIO_PUBLICO.iterdir())
    return render_template("index.html", arquivos=arquivos)


@app.route("/arquivos/<nome>")
def baixar(nome):
    try:
        return send_from_directory(DIRETORIO_PUBLICO, nome)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
