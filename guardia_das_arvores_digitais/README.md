# Guardiã das Árvores Digitais

## Visão geral
Radia Perlman revolucionou o roteamento de camada 2 ao criar o Spanning Tree Protocol. Neste desafio, você
recebe acesso a um painel de diagnóstico que expõe os dados de eleição do domínio STP da frota de switches do
laboratório. Seu objetivo é determinar qual dispositivo mantém a prioridade mais baixa e, com isso, provar ao
sistema que você identificou corretamente o root bridge.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Guardiã das Árvores Digitais | `CTF{Arvores_Digitais_Seguras}` | 180 |

## Execução
1. A aplicação Flask é exposta na porta `8080`.; Endpoints relevantes:; `GET /topology` — retorna o inventário completo de switches e seus atributos.; `GET /bridge/` — consulta individual, útil para validar prioridades e endereços MAC.; `GET /flag` — exige o header `X-Root-Bridge` contendo o identificador do switch raiz no formato `prioridade.MAC`.; Utilize ferramentas como `curl` ou `httpie` para experimentar rapidamente.
2. A flag segue o formato `CTF{...}` e é validada diretamente pela aplicação quando o header correto é enviado.

## Narrativa
Explorar Guardiã das Árvores Digitais revela a flag quando a vulnerabilidade principal é compreendida e explorada.
