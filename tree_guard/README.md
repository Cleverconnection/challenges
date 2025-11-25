# Tree Guard

## Visão geral
A faceta guardiã de Radia Perlman entra em ação neste exercício. Você recebeu o log de
BPDUs observados por um sensor acadêmico e precisa identificar a tentativa de um "root
falso" se infiltrar na eleição.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Tree Guard | `CECYBER{falsa_root_00:11:22:33:44:99}` | 150 |

## Execução
1. API na porta `8080`.; Endpoints principais:; `GET /` — contexto da investigação.; `GET /trace` — retorna o log `tree_guard_trace.txt` com comentários originais.; `GET /analysis` — resume os campos suspeitos destacados pela equipe de Radia.; `POST /verify` — aceita `{"flag": "..."}` no formato exigido.
2. Descubra o endereço MAC utilizado no golpe e envie `CECYBER{falsa_root_}` para validar.

## Narrativa
Explorar Tree Guard revela a flag quando a vulnerabilidade principal é compreendida e explorada.
