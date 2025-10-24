# A02 — Corrida pelo Controle

## Visão geral
Dois subsistemas competem pela atualização do estado de navegação e geram resultados inconsistentes sem sincronização. A missão relembra o alerta de Margaret Hamilton sobre a precisão necessária para cada linha de código. O participante deve observar o log em `/var/log/navegadora/corrida.log` e habilitar a trava de coordenação no arquivo `config/controle_navegacao.json`.

## Tabela de referência interna

| Desafio | Flag | Pontuação |
| ------- | ----- | --------- |
| Corrida pelo Controle | `CTF{condicao_de_corrida_domada}` | 10 |

## Execução
1. Iniciar a instância do desafio.
2. Ler os avisos do log sobre inconsistências.
3. Ajustar o parâmetro `usar_trava` para garantir estabilidade.

## Narrativa
> "O software deve conduzir a missão com previsibilidade absoluta." — Margaret Hamilton

Somente após sincronizar as threads a missão alcança estabilidade e registra a flag.
