# Tree Guard — Write-up

## Descrição
O serviço entrega o log dos BPDUs observados por um sensor e destaca uma possível fraude.
O participante deve identificar o endereço MAC do suposto atacante e enviar a flag no
formato solicitado.

## Passos de solução
1. Acessar `/trace` para baixar o arquivo `tree_guard_trace.txt`.
2. Notar que as duas primeiras linhas indicam o root legítimo (`00:11:22:33:44:55`) e um
   designado (`00:11:22:33:44:66`).
3. A terceira linha demonstra um quadro com `root=00:11:22:33:44:99`, igual ao endereço de origem,
   o que caracteriza um ataque de spoofing de root.
4. Enviar `{"flag": "CECYBER{falsa_root_00:11:22:33:44:99}"}` para `/verify`.

## Pontuação
Requer leitura atenta do log e conhecimento de ataque STP spoofing. Pontuação sugerida:
150 pontos.

## Flag
`CECYBER{falsa_root_00:11:22:33:44:99}` — valor aceito pelo verificador.
