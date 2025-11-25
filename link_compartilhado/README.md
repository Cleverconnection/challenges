# Link Compartilhado

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Link Compartilhado | `CTF{creds_in_query}` | Fácil |

## Execução
1. Um link de backup foi compartilhado com um token na própria query string e continua válido para automações sem expiração.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Localizar o link com token válido e utilizá-lo para recuperar a flag.
4. `CTF{creds_in_query}`
5. Procure um link com `?token=` na página inicial.

## Narrativa
Explorar Link Compartilhado revela a flag quando a vulnerabilidade principal é compreendida e explorada.
