import json
import logging
import threading
import time
from pathlib import Path

CONFIG_PATH = Path('/app/config/controle_navegacao.json')
LOG_DIR = Path('/var/log/navegadora')
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / 'corrida.log'

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s | %(threadName)s | %(message)s',
)

FLAG = 'CTF{condicao_de_corrida_domada}'
QUOTE = 'Margaret Hamilton dizia: "O software deve conduzir a missão com previsibilidade absoluta."'

estado = {
    'altitude': 0,
    'velocidade': 0,
    'integridade': [],
}

estado_lock = threading.Lock()


def carregar_config():
    with CONFIG_PATH.open('r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def ajustar_altitude(config):
    for _ in range(1000):
        if config['usar_trava']:
            with estado_lock:
                estado['altitude'] += 1
        else:
            estado['altitude'] += 1
        time.sleep(0.001)


def ajustar_velocidade(config):
    for _ in range(1000):
        if config['usar_trava']:
            with estado_lock:
                estado['velocidade'] += 2
                estado['integridade'].append('nav-ok')
        else:
            estado['velocidade'] += 2
            estado['integridade'].append('nav-race')
        time.sleep(0.001)


def verificar_estabilidade(config):
    while True:
        time.sleep(0.5)
        if config['usar_trava']:
            with estado_lock:
                altitude = estado['altitude']
                velocidade = estado['velocidade']
                integridade = list(estado['integridade'])
        else:
            altitude = estado['altitude']
            velocidade = estado['velocidade']
            integridade = list(estado['integridade'])

        if altitude >= 1000 and velocidade >= 2000 and integridade.count('nav-ok') >= 900:
            logging.info('%s | Estado sincronizado. Altitude=%s Velocidade=%s', QUOTE, altitude, velocidade)
            mensagem = (
                'Missão estabilizada sem condição de corrida. Registrando na cápsula: '
                f'{FLAG}'
            )
            logging.info(mensagem)
            print(mensagem)
            break
        logging.warning(
            'Controle descompassado. Altitude=%s Velocidade=%s Integridade_ok=%s',
            altitude,
            velocidade,
            integridade.count('nav-ok'),
        )


def main():
    config = carregar_config()
    logging.info('Iniciando sequências de navegação. %s', QUOTE)

    altitude_thread = threading.Thread(target=ajustar_altitude, args=(config,), name='Altitude')
    velocidade_thread = threading.Thread(target=ajustar_velocidade, args=(config,), name='Velocidade')
    monitor_thread = threading.Thread(target=verificar_estabilidade, args=(config,), name='Monitor')

    altitude_thread.start()
    velocidade_thread.start()
    monitor_thread.start()

    monitor_thread.join()


if __name__ == '__main__':
    main()
