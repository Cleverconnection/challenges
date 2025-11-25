# Compartilhamento Cruzado

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Compartilhamento Cruzado | `CTF{cors_wildcard_token}` | Fácil |

## Execução
1. Uma API foi publicada com configuração CORS permissiva, permitindo que páginas externas leiam respostas autenticadas do navegador do usuário.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Demonstrar a leitura indevida e usar o artefato exposto para recuperar a flag.
4. `CTF{cors_wildcard_token}`
5. Verifique cabeçalhos CORS e tente ler dados autenticados a partir de outra origem.

## Narrativa
Explorar Compartilhamento Cruzado revela a flag quando a vulnerabilidade principal é compreendida e explorada.
