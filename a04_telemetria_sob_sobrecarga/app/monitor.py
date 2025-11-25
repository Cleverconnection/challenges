import json
import logging
import time
from pathlib import Path

CONFIG_PATH = Path('/app/config/config.json')
TELEMETRY_PATH = Path('/data/telemetry.log')
LOG_DIR = Path('/var/log/navegadora')
LOG_DIR.mkdir(parents=True, exist_ok=True)
MONITOR_LOG = LOG_DIR / 'monitor.log'

FLAG = 'CTF{telemetria_em_modo_safe}'
QUOTE = (
    'Margaret Hamilton reforçava: "Precisamos estar preparadas para todas as anomalias."'
)

logging.basicConfig(
    filename=str(MONITOR_LOG),
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
)


def carregar_config():
    with CONFIG_PATH.open('r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def registrar_linha(mensagem):
    TELEMETRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TELEMETRY_PATH.open('a', encoding='utf-8') as arquivo:
        arquivo.write(mensagem + '\n')


def monitorar():
    logging.info('Monitorando telemetria com filosofia de Hamilton.')
    aviso_emitido = False
    while True:
        config = carregar_config()
        modo = config.get('modo', 'DEGRADED')
        prioridade_nav = config.get('prioridade_nav_control', 5)
        prioridade_dados = config.get('prioridade_coleta_dados', 2)

        if modo == 'SAFE_FLIGHT' and prioridade_nav <= prioridade_dados:
            mensagem = (
                'SAFE_FLIGHT restaurado. NAV_SAFE ativo com prioridade=%s. Sinalização completa: %s'
                % (prioridade_nav, FLAG)
            )
            registrar_linha(mensagem)
            logging.info(mensagem)
            break

        if not aviso_emitido:
            registrar_linha(
                'ALERTA: NAV_SAFE abortada por saturação. Ajuste prioridades no config.json para modo SAFE_FLIGHT.'
            )
            aviso_emitido = True

        logging.warning(
            '%s Estado atual: modo=%s prioridade_nav=%s prioridade_dados=%s',
            QUOTE,
            modo,
            prioridade_nav,
            prioridade_dados,
        )
        time.sleep(5)


if __name__ == '__main__':
    monitorar()
