# Tree Guard

A faceta guardiã de Radia Perlman entra em ação neste exercício. Você recebeu o log de
BPDUs observados por um sensor acadêmico e precisa identificar a tentativa de um "root
falso" se infiltrar na eleição.

## Acesso ao serviço

- API na porta `8080`.
- Endpoints principais:
  - `GET /` — contexto da investigação.
  - `GET /trace` — retorna o log `tree_guard_trace.txt` com comentários originais.
  - `GET /analysis` — resume os campos suspeitos destacados pela equipe de Radia.
  - `POST /verify` — aceita `{"flag": "..."}` no formato exigido.

## Flag

Descubra o endereço MAC utilizado no golpe e envie `CECYBER{falsa_root_<mac>}` para
validar.
