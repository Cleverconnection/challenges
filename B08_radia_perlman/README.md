# STP Loop Recovery

Radia Perlman usa este laboratório para demonstrar como o Spanning Tree Protocol decide
qual enlace deve ser podado quando surge um loop. A API expõe todos os detalhes para você
reproduzir a análise sem depender de uma console interativa.

## Acesso ao serviço

- A aplicação Flask responde na porta `8080`.
- Endpoints principais:
  - `GET /topology` — descreve os bridges e enlaces ativos.
  - `GET /states` — lista o papel de cada porta e o estado atual.
  - `GET /metrics` — apresenta contadores de BPDUs por interface.
  - `POST /verify` — valida a flag.

## Flag

Após descobrir a interface bloqueada, envie `CTF{loop_blocked_successfully}` no endpoint `POST /verify`.
