# Root Bridge Live

Radia Perlman orienta os trainees do laboratório com uma timeline detalhada de reconvergência.
A API do desafio reproduz cada passo da eleição e permite que você valide a interpretação sem
precisar rodar comandos interativos.

## Acesso ao serviço

- A aplicação Flask responde na porta `8080`.
- Endpoints principais:
  - `GET /lab` — descreve os bridges e enlaces virtuais.
  - `GET /timeline` — registra os eventos capturados durante a reconvergência.
  - `GET /hints` — relembra critérios de desempate.
  - `POST /verify` — aceita a flag via JSON.

## Flag

A flag esperada é `CTF{root_change_detected}` após identificar com precisão o instante da troca de raiz.
