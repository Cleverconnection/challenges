from flask import Flask, render_template, request, make_response

app = Flask(__name__)

FLAG = "CTF{Trinity_Glitch_Vigilia}"


@app.route("/")
def index():
    consulta = request.args.get("q", "")
    resposta = make_response(render_template("index.html", consulta=consulta))
    resposta.set_cookie("fragmento_oraculo", FLAG)
    return resposta


@app.route("/memoria")
def memoria():
    return render_template("memoria.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
