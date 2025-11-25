import json
import logging
import time
from pathlib import Path

CONFIG_PATH = Path('/app/config/controle_loop.json')
LOG_DIR = Path('/var/log/navegadora')
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / 'loop.log'

FLAG = 'CTF{loop_infinito_corrigido}'

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
)

QUOTE = (
    'Margaret Hamilton lembrava sempre: "Tolerância zero a falhas, porque vidas estão em jogo."'
)


def carregar_configuracao():
    try:
        with CONFIG_PATH.open('r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        logging.error('Configuração ausente. Sem os dados corretos, ficamos presos no ciclo.')
        return {}
    except json.JSONDecodeError as err:
        logging.error('Configuração corrompida: %s', err)
        return {}


def registrar_estado(mensagem, nivel='info'):
    texto = f"{mensagem} | {QUOTE}"
    if nivel == 'warning':
        logging.warning(texto)
    elif nivel == 'error':
        logging.error(texto)
    else:
        logging.info(texto)


def main():
    registrar_estado('Inicializando controle de laço lunar para a Navegadora.')
    while True:
        configuracao = carregar_configuracao()
        sentinela = configuracao.get('sentinela_laco', 'travado')
        estado_atual = configuracao.get('estado_atual', 'ORBITA_CAOTICA')

        if sentinela.upper() == 'LIBERADO' and estado_atual == 'ORBITA_ESTAVEL':
            registrar_estado(
                'Sentinela liberada e órbita estabilizada. Hamilton sorri ao ver a missão segura.'
            )
            mensagem_flag = (
                'Sequência de correção concluída com sucesso. Registro de missão autenticado: '
                f'{FLAG}'
            )
            logging.info(mensagem_flag)
            print(mensagem_flag)
            break

        registrar_estado(
            f'Loop ainda ativo: sentinela={sentinela}, estado_atual={estado_atual}. '
            'Ajuste o arquivo de configuração para liberar a rotina.',
            nivel='warning',
        )
        time.sleep(2)


if __name__ == '__main__':
    main()
