import json
from pathlib import Path

from flask import Flask, render_template

CONFIG_PATH = Path('/app/config/config.json')
TELEMETRY_PATH = Path('/data/telemetry.log')

app = Flask(__name__)


def carregar_config():
    with CONFIG_PATH.open('r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def carregar_log(limite=10):
    if not TELEMETRY_PATH.exists():
        return []
    linhas = TELEMETRY_PATH.read_text(encoding='utf-8').strip().splitlines()
    return linhas[-limite:]


@app.route('/')
def painel():
    config = carregar_config()
    log = carregar_log()
    return render_template('painel.html', config=config, log=log)


@app.route('/memoria')
def memoria():
    config = carregar_config()
    return render_template('memoria.html', config=config)


@app.route('/trajetoria')
def trajetoria():
    log = carregar_log(limite=20)
    return render_template('trajetoria.html', log=log)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
