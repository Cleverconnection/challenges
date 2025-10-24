# Tree Guard

Radia Perlman insiste que a estabilidade do Spanning Tree depende de vigiar quem tenta se
passar pela raiz. Este desafio entrega uma coleta textual de BPDUs para que você identifique
o atacante.

## Acesso ao serviço

- A aplicação Flask responde na porta `8080`.
- Endpoints principais:
  - `GET /trace` — baixa o arquivo `tree_guard_trace.txt` com os registros capturados.
  - `GET /analysis` — resume os papéis legítimos e o motivo da suspeita.
  - `POST /verify` — recebe a flag.

## Flag

Descubra o endereço MAC utilizado no golpe e envie `CTF{falsa_root_<mac>}` para confirmar a resposta.
