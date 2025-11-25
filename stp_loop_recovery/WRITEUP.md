# STP Loop Recovery — Write-up

## Objetivo
Determinar qual porta entrou em estado blocking durante a recuperação do loop.

## Solução
1. Consultar `/topology` para visualizar os bridges `switch-ivy` e `switch-nile` com dois enlaces
   cruzados.
2. Em `/states`, notar que a porta `switch-ivy:eth1` está marcada como `role=alternate` e
   `state=blocking`, enquanto as demais continuam como `designated` ou `root`.
3. Confirmar em `/metrics` que a métrica acumulada para o enlace `eth1` é mais alta, justificando o
   bloqueio.
4. Enviar `{"flag": "CECYBER{loop_blocked_successfully}"}` para `/verify` e obter a flag.

## Pontuação
Requer interpretar a tabela STP e entender a diferença entre funções de porta. Dificuldade
média: 150 pontos.

## Flag
`CECYBER{loop_blocked_successfully}` — única resposta aceita.
