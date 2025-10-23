# Guardiã das Árvores Digitais — Write-up

## Visão Geral

O serviço expõe uma API simples que retorna a topologia de uma rede fictícia rodando Spanning Tree Protocol.
Cada nó possui os campos `priority` e `mac`. O código Python calcula internamente o `ROOT_BRIDGE_ID` por meio de
`min(nodes, key=(priority, mac))`. Portanto, basta replicar a mesma lógica no cliente.

## Passo a Passo

1. Acesse `GET /topology` e colete a lista de switches.
2. Ordene pelos campos `priority` e `mac`. O menor valor é `4096.00:11:22:33:44:55`, referente ao `switch-alpha`.
3. Envie uma requisição `GET /flag` com o header `X-Root-Bridge: 4096.00:11:22:33:44:55`.
4. O servidor retorna a flag `CTF{Arvores_Digitais_Seguras}`.

## Justificativa da Pontuação

O desafio exige entendimento básico de como STP elege o root bridge, mas a implementação é curta e pode ser
resolvida com um script simples ou até manualmente. O nível de dificuldade corresponde a um desafio introdutório
(aprox. 150 pontos).

## Flags Aceitas

- `CTF{Arvores_Digitais_Seguras}` — valor padrão do container.
- Instâncias podem sobrescrever a flag via variável de ambiente `FLAG`.
