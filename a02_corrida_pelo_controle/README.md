# Corrida pelo Controle

## Visão geral
Dois subsistemas competem pela atualização do estado de navegação e geram resultados inconsistentes sem sincronização. A missão relembra o alerta de Margaret Hamilton sobre a precisão necessária para cada linha de código. O participante deve observar o log em `/var/log/navegadora/corrida.log` e habilitar a trava de coordenação no arquivo `config/controle_navegacao.json`.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Corrida pelo Controle | `CTF{condicao_de_corrida_domada}` | Fácil |

## Execução
1. Iniciar a instância do desafio. 2. Ler os avisos do log sobre inconsistências. 3. Ajustar o parâmetro `usar_trava` para garantir estabilidade.
2. Somente após sincronizar as threads a missão alcança estabilidade e registra a flag.

## Narrativa
> "O software deve conduzir a missão com previsibilidade absoluta." — Margaret Hamilton

Explorar Corrida pelo Controle revela a flag quando a vulnerabilidade principal é compreendida e explorada.
