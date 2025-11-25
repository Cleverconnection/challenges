# A04 — Telemetria Sob Sobrecarga

## Visão geral
Uma interface Flask apresenta a sala de controle da Navegadora Lunar em três páginas, todas em tons de laranja. O monitor de telemetria registra que o subsistema `NAV_SAFE` é abortado devido a prioridades erradas. O participante deve analisar `/data/telemetry.log`, ajustar `config/config.json` e aguardar o monitor entrar em modo `SAFE_FLIGHT`.

## Tabela de referência interna

| Desafio | Flag | Pontuação |
| ------- | ----- | --------- |
| Telemetria Sob Sobrecarga | `CTF{telemetria_em_modo_safe}` | 15 |

## Execução
1. Iniciar o container e acessar a aplicação web na porta 5000.
2. Ler os alertas nas páginas Painel, Memória e Trajetória.
3. Ajustar `modo` para `SAFE_FLIGHT` e reduzir `prioridade_nav_control` no arquivo de configuração.
4. Monitorar o log até que seja registrada a restauração com a flag.

## Narrativa
> "Precisamos estar preparadas para todas as anomalias." — Margaret Hamilton

Quando `NAV_SAFE` recebe prioridade adequada, o monitor escreve no log a confirmação e a flag.
