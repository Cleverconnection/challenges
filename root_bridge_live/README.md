# Root Bridge Live

Radia Perlman defendia que entender STP exigia observar o protocolo "respirar". Este
laboratório registra uma sessão de reconvergência em tempo real para que você acompanhe
os eventos como se estivesse com um sniffer ligado no console.

## Acesso ao serviço

- Serviço Flask exposto na porta `8080`.
- Endpoints principais:
  - `GET /` — apresenta o resumo da atividade.
  - `GET /lab` — descreve a quantidade de bridges, suas prioridades e enlaces ativos.
  - `GET /timeline` — exibe o fluxo de mensagens BPDU ordenado por timestamp.
  - `GET /hints` — relembra como comparar prioridade e MAC para detectar o root.
  - `POST /verify` — recebe um JSON `{"flag": "..."}` com sua conclusão.

## Flag

A flag esperada é `CECYBER{root_change_detected}` após identificar com precisão o
momento de troca da raiz na linha do tempo.
