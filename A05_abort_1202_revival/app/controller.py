import json
import logging
import subprocess
import time
from pathlib import Path

CONFIG_PATH = Path('/app/config/prioridades.json')
CORE_PATH = Path('/app/bin/rt_core')
LOG_DIR = Path('/var/log/navegadora')
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / 'abort1202.log'

FLAG = 'CTF{abort_1202_superado}'
QUOTE = (
    'Margaret Hamilton lembrava a equipe: "Nunca deixem que uma interrupção inesperada derrube o sistema."'
)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
)


def carregar_config():
    with CONFIG_PATH.open('r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def executar_ciclo():
    while True:
        config = carregar_config()
        ambiente = {
            'NAV_PRIORITY': str(config.get('prioridade_nav', 4)),
            'DSKY_PRIORITY': str(config.get('prioridade_interface', 3)),
            'TASK_BURST': str(config.get('carga_interruptores', 120)),
        }
        logging.warning(
            '%s NAV=%s DSKY=%s BURST=%s',
            QUOTE,
            ambiente['NAV_PRIORITY'],
            ambiente['DSKY_PRIORITY'],
            ambiente['TASK_BURST'],
        )
        resultado = subprocess.run(
            [str(CORE_PATH)],
            env={
                **ambiente,
                **{
                    'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
                },
            },
            capture_output=True,
            text=True,
        )

        logging.info('Saída do núcleo: %s', resultado.stdout.strip())

        if resultado.returncode == 0 and FLAG in resultado.stdout:
            logging.info('Abort 1202 contido. Flag registrada: %s', FLAG)
            print(resultado.stdout.strip())
            break

        logging.error('Núcleo retornou código %s. Reavalie prioridades em %s.', resultado.returncode, CONFIG_PATH)
        time.sleep(5)


if __name__ == '__main__':
    executar_ciclo()
