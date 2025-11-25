# Depuradora do Mark I

## Visão geral
Grace Hopper foi pioneira em tornar computadores compreensíveis para humanos. Nesta simulação, você assume o papel
de engenheira responsável por analisar o log de fitas do Harvard Mark I, remontar o código secreto e liberar o
patch final escrito em homenagem ao FLOW-MATIC.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Depuradora do Mark I | `CTF{Flowmatic_Debug_Master}` | – |

## Execução
1. Serviço Flask escutando na porta `8080`.; Rotas:; `GET /console` devolve o log das fitas. Cada linha destaca a letra necessária para compor o comando.; `GET /punchcard?opcode=...` valida o código reconstruído. O valor precisa ser informado em caixa alta.; As letras iniciais do log formam o nome da linguagem celebrada por Hopper. Utilize uma ferramenta como `curl` (`curl "$URL/punchcard?opcode=FLOW-MATIC"`) para enviar o comando final.
2. O serviço retorna a flag no formato `CTF{...}` quando o opcode correto é informado.

## Narrativa
Explorar Depuradora do Mark I revela a flag quando a vulnerabilidade principal é compreendida e explorada.
