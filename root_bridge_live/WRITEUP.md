# Root Bridge Live — Write-up

## Resumo
O desafio fornece dados estruturados que representam um laboratório STP monitorado. A
solução consiste em acompanhar a linha do tempo dos BPDUs para perceber quando um novo
root bridge assume o domínio.

## Guia de solução
1. Solicitar `/lab` para entender os dispositivos: `switch-alpha` (prioridade 4096) e
   `switch-orion` (prioridade 4096) conectados por dois enlaces redundantes.
2. Consultar `/timeline` para obter a sequência de eventos. A entrada com timestamp `12.5` mostra
   que `switch-orion` envia um BPDU com prioridade igual porém MAC inferior (`00:11:22:33:44:41`).
3. Identificar que a mensagem "root takeover" indica a troca da raiz. As demais entradas confirmam
   o bloqueio da porta `eth1` para evitar loop.
4. Enviar `{"flag": "CECYBER{root_change_detected}"}` para `/verify` e receber a flag.

## Pontuação
Requer análise interpretativa dos eventos STP, mas não envolve exploração complexa. Pontuação
recomendada: 150 pontos.

## Flag
`CECYBER{root_change_detected}` — valor único aceito.
