# Patch Indireto

## Visão geral
A API de perfil aceita atualizações via `PATCH /api/users/me` e implementa compatibilidade com um formato legado em que o campo `role` é uma string simples. Essa compatibilidade permite sobrescrever o objeto de role e definir diretamente `admin`.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Patch Indireto | `CTF{api_privilege_escalation}` | Médio |

## Execução
1. Analisar operações PATCH em APIs REST.; Reconhecer campos polimórficos que aceitam mais de um tipo.; Escalar privilégios forjando payloads diferenciados.
2. `GET /api/users/me` — Retorna o objeto de usuário atual.; `PATCH /api/users/me` — Atualiza campos do usuário sem validação adequada.; `GET /flag` — Entregue apenas quando a role for `admin`.
3. Levante o container do desafio. 2. Requisite `/api/users/me` para observar o formato inicial. 3. Envie um PATCH com `{"role":"admin"}`.
4. Após atualizar a role para string `admin`, consulte `/flag` e receba a flag do desafio.

## Narrativa
Explorar Patch Indireto revela a flag quando a vulnerabilidade principal é compreendida e explorada.
