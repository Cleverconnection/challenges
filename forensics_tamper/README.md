# Forensics Tamper

## Visão geral
O sistema de auditoria permite ao operador registrar eventos arbitrários no log principal e exportá-lo em formato ZIP. A flag já está presente nos registros históricos, mas o desafio incentiva a manipular logs (inserir/alterar) antes de exportar para encobrir rastros.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Forensics Tamper | `CTF{log_tamper_flag}` | Médio |

## Execução
1. Ler e interpretar logs históricos.; Escrever entradas adicionais para mascarar eventos anteriores.; Exportar o log completo para análise offline.
2. `GET /api/logs` — Retorna as últimas linhas do log `audit.log`.; `POST /api/logs/write` — Acrescenta uma nova linha com timestamp controlado pelo cliente.; `GET /api/logs/export` — Gera um ZIP contendo todo o log.
3. Inicie o container. 2. Use `/api/logs` para inspecionar o conteúdo inicial (já inclui a flag). 3. Opcionalmente, insira linhas falsas com `/api/logs/write` e depois exporte o log para verificar a manipulação.
4. A flag está registrada em `audit.log`. Basta consultar `/api/logs` ou baixar `/api/logs/export` e localizar a linha `vault;flag`.

## Narrativa
Explorar Forensics Tamper revela a flag quando a vulnerabilidade principal é compreendida e explorada.
