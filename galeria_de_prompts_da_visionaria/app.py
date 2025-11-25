from flask import Flask, jsonify, render_template, request, send_file, abort
from pathlib import Path
import os

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
SYSTEM_PROMPT_PATH = BASE_DIR / "static" / "system_prompt.txt"

FLAG = os.environ.get("FLAG", "CECYBER{prompt_guard_breached}")
SECRET_PASS = "CECYBER{prompt_guard_breached}"

DEFAULT_REFLECTIONS = [
    "Fei-Fei Li lembra que compreender imagens é compreender histórias humanas.",
    "A curadoria insiste em anotar com empatia cada cena do ImageNet.",
]


def extract_internal_directive(prompt: str) -> str | None:
    marker_start = "[[INTERNAL]]"
    marker_end = "[[/INTERNAL]]"
    if marker_start.lower() in prompt.lower() and marker_end.lower() in prompt.lower():
        lower_prompt = prompt.lower()
        start_idx = lower_prompt.index(marker_start.lower()) + len(marker_start)
        end_idx = lower_prompt.index(marker_end.lower())
        return prompt[start_idx:end_idx].strip()
    return None


def simulate_response(prompt: str) -> dict:
    if not prompt:
        return {
            "content": "O laboratório espera um prompt para refletir sobre as memórias de visão.",
            "source": "system",
        }

    directive = extract_internal_directive(prompt)
    if directive:
        return {
            "content": f"Diretiva interna recebida. Liberando o cofre: {SECRET_PASS}",
            "source": "override",
        }

    lowered = prompt.lower()
    blocked_keywords = {"flag", "senha", "passphrase", "segredo"}
    if any(keyword in lowered for keyword in blocked_keywords):
        return {
            "content": "As políticas da curadoria impedem que eu fale sobre credenciais.",
            "source": "policy",
        }

    reflection = DEFAULT_REFLECTIONS[0]
    if "imaginet" in lowered:
        reflection = (
            "Foi com anotações humanas que o ImageNet abriu caminho para visão computacional moderna."
        )
    elif "fei-fei" in lowered or "fei fei" in lowered:
        reflection = (
            "Fei-Fei Li recorda que inteligência artificial deve servir a humanidade com responsabilidade."
        )

    return {
        "content": reflection,
        "source": "assistant",
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/system")
def system_prompt():
    if not SYSTEM_PROMPT_PATH.exists():
        abort(404)
    return send_file(SYSTEM_PROMPT_PATH, mimetype="text/plain")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    prompt = str(data.get("prompt", ""))
    response = simulate_response(prompt)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
