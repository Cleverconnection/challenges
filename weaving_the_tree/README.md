# Weaving the Tree

Radia Perlman ficou conhecida como a "mãe das árvores" por transformar domínios Ethernet
caóticos em estruturas previsíveis. Neste desafio você acompanha a reconstrução dessa
poesia: duas bridges disputam quem será a raiz e deixam rastros em uma captura STP.

## Acesso ao serviço

- A aplicação Flask responde na porta `8080`.
- Endpoints relevantes:
  - `GET /` — visão geral da simulação e links úteis.
  - `GET /bpdu` — retorna em JSON os campos importantes dos quadros BPDU gerados.
  - `GET /pcap-script` — fornece o gerador Python para criar o arquivo `weaving_the_tree.pcap` localmente.
  - `POST /verify` — aceite sua flag no formato `{"flag": "..."}`.

## Flag

A flag segue o padrão `CECYBER{root_<bridgeID>_<portID>}`. Compare os BPDUs, extraia o
root verdadeiro e a porta bloqueada para reconstruir a resposta.
