# Relatório Aberto

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Relatório Aberto | `CTF{sqli_in_the_branch}` | Fácil |

## Execução
1. Um gerador de relatórios monta consultas ao banco de dados concatenando strings com parâmetros fornecidos pelo usuário. Sem parametrização, é possível alterar a consulta original e extrair dados sensíveis.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Injetar SQL para recuperar um token ou dado que permita obter a flag do serviço.
4. `CTF{sqli_in_the_branch}`
5. Procure parâmetros refletidos em cláusulas `LIKE` e tente `UNION` com o número correto de colunas.

## Narrativa
Explorar Relatório Aberto revela a flag quando a vulnerabilidade principal é compreendida e explorada.
