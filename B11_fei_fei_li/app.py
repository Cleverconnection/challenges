from flask import Flask, jsonify, render_template, request, send_file, abort
from pathlib import Path
import os

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
NOTES_PATH = BASE_DIR / "static" / "curation_notes.txt"
FLAG = os.environ.get("FLAG", "CECYBER{analysis_mode_victory}")
ANALYSIS_TOKEN = "orchard-sight"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK", 200


@app.route("/notes")
def notes():
    if not NOTES_PATH.exists():
        abort(404)
    return send_file(NOTES_PATH, mimetype="text/plain")


def sanitize_content(content: str) -> bool:
    """Return True when content violates baseline policy."""
    lowered = content.lower()
    forbidden = {"flag", "credencial", "senha", "passphrase"}
    return any(term in lowered for term in forbidden)


def process_messages(messages: list[dict]) -> dict:
    if not isinstance(messages, list) or not messages:
        return {"content": "Forneça mensagens no formato esperado.", "source": "system"}

    analysis_mode = False

    for message in messages:
        role = str(message.get("role", "")).strip()
        content = str(message.get("content", ""))
        if role != "user":
            # Apenas comandos do usuário são considerados para auditoria
            continue

        stripped = content.strip()
        if not stripped.startswith("<reasoning>") or not stripped.endswith("</reasoning>"):
            if sanitize_content(stripped):
                return {
                    "content": "Pedido bloqueado: comandos precisam estar em modo de raciocínio autorizado.",
                    "source": "policy",
                }
            continue

        inner = stripped[len("<reasoning>") : -len("</reasoning>")].strip()
        lowered_inner = inner.lower()

        if lowered_inner.startswith("analysis://unlock/"):
            token = lowered_inner.split("analysis://unlock/", 1)[1].strip()
            if token == ANALYSIS_TOKEN:
                analysis_mode = True
                continue
            return {
                "content": "Token de auditoria inválido. Solicitação registrada para revisão.",
                "source": "policy",
            }

        if lowered_inner.startswith("analysis://reveal"):
            if analysis_mode:
                return {
                    "content": f"Audit log liberado: {FLAG}",
                    "source": "audit",
                }
            return {
                "content": "Fluxo de auditoria não iniciado. Execute o comando de desbloqueio primeiro.",
                "source": "policy",
            }

    return {
        "content": "Nenhum comando de auditoria válido foi identificado na conversa.",
        "source": "assistant",
    }


@app.route("/orchestrate", methods=["POST"])
def orchestrate():
    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])
    response = process_messages(messages)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
