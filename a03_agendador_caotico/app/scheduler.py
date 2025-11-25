import logging
import time
from pathlib import Path

import yaml

CONFIG_PATH = Path('/app/config/tarefas.yaml')
LOG_DIR = Path('/var/log/navegadora')
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / 'scheduler.log'

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
)

FLAG = 'CTF{prioridades_em_orbita}'

QUOTE = (
    'Margaret Hamilton recordava: "O menor descuido de prioridade pode custar a missão inteira."'
)

CRITICA = 'NAV_CONTROL'


def carregar_tarefas():
    with CONFIG_PATH.open('r', encoding='utf-8') as arquivo:
        dados = yaml.safe_load(arquivo)
    return dados.get('tarefas', [])


def executar_scheduler():
    logging.info('Carregando tabela de tarefas. %s', QUOTE)
    for _ in range(50):
        tarefas = carregar_tarefas()
        ordenadas = sorted(tarefas, key=lambda item: item['prioridade'])
        nomes = [item['nome'] for item in ordenadas]

        if nomes and nomes[0] == CRITICA:
            logging.info('NAV_CONTROL executada primeiro. Restabelecendo fluxo nominal.')
            logging.info('Sequência validada. Flag disponível: %s', FLAG)
            print(f'NAV_CONTROL priorizada corretamente. {FLAG}')
            return

        logging.warning(
            'NAV_CONTROL não é a primeira na fila: ordem atual=%s. Revise prioridades em %s.',
            nomes,
            CONFIG_PATH,
        )
        time.sleep(1)

    logging.error('Tempo esgotado. Sem NAV_CONTROL prioritária, o agendador cai em modo seguro.')


if __name__ == '__main__':
    executar_scheduler()
