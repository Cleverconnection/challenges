# Saldo Negativo Corrida

## Visão geral
O endpoint de saque consulta o saldo e, antes de subtrair o valor, espera 0,6s. Enquanto isso, outras requisições podem executar a mesma verificação e resultar em saldo negativo.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Saldo Negativo Corrida | `CTF{race_negative_balance}` | Médio |

## Execução
1. Simular condições de corrida em operações de débito.; Combinar múltiplos clientes simultâneos contra o mesmo endpoint.; Observar o impacto da falta de bloqueio pessimista.
2. `GET /api/state` — Retorna o saldo atual das contas (`checking`, `credit`).; `POST /api/withdraw` — Permite saques sem sincronização adequada.; `GET /flag` — Retorna a flag quando `checking` fica negativo.
3. Inicie o container. 2. Planeje saques de valor alto (ex.: 1000). 3. Dispare duas ou mais requisições simultâneas.
4. Envie duas requisições `POST /api/withdraw` com `{"amount": 1000}` ao mesmo tempo.; O saldo cairá para -500 e `/flag` retornará a flag.

## Narrativa
Explorar Saldo Negativo Corrida revela a flag quando a vulnerabilidade principal é compreendida e explorada.
