# Guardiã das Árvores Digitais

Radia Perlman revolucionou o roteamento de camada 2 ao criar o Spanning Tree Protocol. Neste desafio, você
recebe acesso a um painel de diagnóstico que expõe os dados de eleição do domínio STP da frota de switches do
laboratório. Seu objetivo é determinar qual dispositivo mantém a prioridade mais baixa e, com isso, provar ao
sistema que você identificou corretamente o <em>root bridge</em>.

## Acesso ao serviço

- A aplicação Flask é exposta na porta `8080`.
- Endpoints relevantes:
  - `GET /topology` — retorna o inventário completo de switches e seus atributos.
  - `GET /bridge/<nome>` — consulta individual, útil para validar prioridades e endereços MAC.
  - `GET /flag` — exige o header `X-Root-Bridge` contendo o identificador do switch raiz no formato
    `prioridade.MAC`.
  - `GET /pcap-script` — disponibiliza um gerador Scapy com BPDUs extras e ruído ARP/DNS/ICMP/TCP.
- Utilize ferramentas como `curl` ou `httpie` para experimentar rapidamente.

## Flag

A flag segue o formato `CTF{...}` e é validada diretamente pela aplicação quando o header correto é enviado.
O script distribuído gera o arquivo `guardian_tree.pcap` para quem deseja confirmar a análise em um
sniffer, mantendo cinco BPDUs e pacotes auxiliares.
