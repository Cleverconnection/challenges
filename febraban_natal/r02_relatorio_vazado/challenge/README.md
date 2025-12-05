# Relatório Vazado

## Visão Geral
**Categoria:** Web  
**Equipe:** Red Team  
**Dificuldade:** Fácil  
**Técnica:** SQL Injection  
**Pontuação:** 10 pontos  
**Formato da flag:** `CTF{*******}`

## Tabela de Referência Interna

| Desafio          | Flag                         | Dificuldade |
| ---------------- | ---------------------------- | ----------- |
| Relatório Vazado | `CTF{vazamento_natalino_sql}` | Fácil       |

## Execução
1. Acesse `/auditoria/search?campo=...`
2. Explore o comportamento do filtro de busca.
3. Encontre um meio de revelar o token administrativo.
4. Valide o token em `/auditoria/validar?token=...`
5. Se o token estiver correto, a flag será exibida.

## Flag
`CTF{vazamento_natalino_sql}`
