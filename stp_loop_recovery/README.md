# STP Loop Recovery

O laboratório homenageia o método de Radia Perlman para explicar o STP: visualizar o
fluxo como uma árvore que se poda sozinha. Aqui, você recebe uma fotografia dos dois
bridges que entraram em guerra com um loop físico e precisa identificar qual porta foi
bloqueada para estabilizar o domínio.

## Acesso ao serviço

- API Flask na porta `8080`.
- Endpoints úteis:
  - `GET /` — introdução narrativa do incidente.
  - `GET /topology` — descreve os bridges, prioridades e vínculos de porta.
  - `GET /states` — lista a tabela STP por porta (role e estado).
  - `GET /metrics` — apresenta custos acumulados para cada enlace.
  - `POST /verify` — aceite da flag usando `{"flag": "..."}`.

## Flag

Após descobrir a interface bloqueada, envie `CECYBER{loop_blocked_successfully}` no
endpoint `/verify` para confirmar a recuperação.
