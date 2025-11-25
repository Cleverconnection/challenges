# Transação Repetida

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Transação Repetida | `CTF{timestamp_replay_attack}` | Fácil |

## Execução
1. O motor de transações aceita o mesmo timestamp diversas vezes dentro de uma janela, acumulando créditos.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Repetir a mesma transação de forma controlada até acionar o retorno que libera a flag.
4. `CTF{timestamp_replay_attack}`
5. Repita a requisição com o mesmo timestamp até atingir o gatilho.

## Narrativa
Explorar Transação Repetida revela a flag quando a vulnerabilidade principal é compreendida e explorada.
