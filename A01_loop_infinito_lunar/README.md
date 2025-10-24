# A01 — Loop Infinito Lunar

## Visão geral
Desafio inspirado na rotina de Margaret Hamilton em plena missão Apollo. O processo de controle fica preso em um laço infinito porque a sentinela de estado não é liberada. O participante precisa analisar os registros em `/var/log/navegadora/loop.log`, interpretar o alerta e ajustar o arquivo `config/controle_loop.json` para levar o sistema ao estado `ORBITA_ESTAVEL` com a sentinela liberada.

## Tabela de referência interna

| Desafio | Flag | Pontuação |
| ------- | ----- | --------- |
| Loop Infinito Lunar | `CTF{loop_infinito_corrigido}` | 10 |

## Execução
1. Iniciar o container.
2. Acompanhar os logs do processo.
3. Ajustar a configuração para eliminar o laço e registrar a órbita estabilizada.

## Narrativa
> "Tolerância zero a falhas, porque vidas estão em jogo." — Margaret Hamilton

Quando o arquivo de configuração é corrigido, o processo imprime a confirmação de correção juntamente com a flag, demonstrando a importância do controle de estados em software crítico.
