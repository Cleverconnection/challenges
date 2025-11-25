# Pagamentos Replay

## Visão geral
O gateway de pagamentos registra transações apenas com base em um identificador fornecido pelo cliente e acumula pontos de fidelidade sem deduplicação. Reenvios do mesmo payload são aceitos indefinidamente, permitindo inflar o saldo de benefícios.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Pagamentos Replay | `CTF{payment_replay_bonus}` | Médio |

## Execução
1. Entender o impacto da ausência de chaves de idempotência.; Realizar ataques de replay repetindo requisições legítimas.; Auditar o histórico (`/api/ledger`) para confirmar a exploração.
2. `POST /api/pay` — Registra um pagamento com `reference`, `amount` e `channel`.; `GET /api/ledger` — Exibe os últimos lançamentos e o total de pontos.; `GET /flag` — Entrega a flag quando a pontuação acumulada for ≥ 5000.
3. Inicie o serviço localmente. 2. Envie um pagamento válido (por exemplo, `{"reference":"fatura-001","amount":1000}`). 3. Reenvie o mesmo corpo diversas vezes utilizando scripts ou repetindo a requisição em ferramentas como Burp.
4. Execute a mesma requisição `POST /api/pay` cinco vezes com `amount` 1000.; O endpoint acumulará 5000 pontos e `/flag` retornará a flag do desafio.

## Narrativa
Explorar Pagamentos Replay revela a flag quando a vulnerabilidade principal é compreendida e explorada.
