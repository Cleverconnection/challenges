# Solução — STP Loop Recovery

## Visão geral
O laboratório disponibiliza a topologia, o estado das portas e contadores de BPDUs. A meta é
identificar qual interface entrou em blocking após a detecção do loop.

## Procedimento sugerido
1. Consultar `GET /states` e filtrar a porta que aparece com `state` igual a `blocking`.
2. Confirmar com `GET /metrics` que a mesma interface reduziu a transmissão de BPDUs.
3. Enviar `{"flag": "CTF{loop_blocked_successfully}"}` para `POST /verify`.

## Resultado
A resposta correta retorna `{"flag": "CTF{loop_blocked_successfully}"}`, confirmando a
interpretação do cenário proposto por Radia Perlman.
