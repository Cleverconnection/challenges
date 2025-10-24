# Solução — Weaving the Tree

## Visão geral
O arquivo `weaving_the_tree.pcap` deve ser gerado localmente executando o script disponível
em `/pcap-script`. O material traz quatro BPDUs que contam a história da troca de root em
uma topologia inspirada nos poemas de Radia Perlman. Pacotes ARP, DNS, ICMP e TCP foram
inseridos como ruído para aproximar a captura de uma rede real.

## Passo a passo

1. Baixar o script: `curl http://<host>:8080/pcap-script -o generate_weaving_pcap.py`.
2. Executar com Scapy instalado: `python generate_weaving_pcap.py`.
3. Abrir o PCAP e filtrar por `llc` ou `stp` para destacar os BPDUs.
4. Identificar o takeover: a bridge `00:11:22:33:44:66` anuncia custo 0 e vence a eleição.
5. Anotar a porta bloqueada informada pelo último BPDU (`Port=0x8000`).
6. Montar a flag `CTF{root_32768_001122334466}` e enviar via `POST /verify` com JSON
   `{"flag": "CTF{root_32768_001122334466}"}`.

## Justificativa da pontuação

O desafio exige familiaridade com STP, leitura de PCAPs e interpretação de ruído de rede.
Os passos são objetivos e contam com dicas gratuitas, justificando pontuação intermediária.
