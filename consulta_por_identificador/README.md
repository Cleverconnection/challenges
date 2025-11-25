# Consulta por Identificador

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Consulta por Identificador | `CTF{idor_bank_accounts}` | Fácil |

## Execução
1. Um serviço de contas expõe um endpoint de consulta por identificador numérico. Sem checagem de posse do recurso, basta variar o ID para obter dados de contas alheias.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Identificar um ID de conta privilegiada e, a partir dos dados expostos, recuperar a flag.
4. `CTF{idor_bank_accounts}`
5. IDs são previsíveis; compare respostas e procure campos extras em contas de alto nível.

## Narrativa
Explorar Consulta por Identificador revela a flag quando a vulnerabilidade principal é compreendida e explorada.
