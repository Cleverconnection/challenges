# Weaving the Tree — Write-up

## Visão geral
O serviço entrega os campos relevantes de dois BPDUs consecutivos e disponibiliza um
script que gera um PCAP idêntico ao utilizado na narrativa. O objetivo é identificar o
root bridge definitivo e a porta que permanece em blocking após a reconvergência.

## Passo a passo da solução
1. Baixar o script em `/pcap-script` e executar localmente (`python generate_weaving_pcap.py`).
2. Abrir `weaving_the_tree.pcap` no Wireshark ou equivalente para ver os campos `Root Identifier`
   e `Port Identifier` nos BPDUs.
3. Observar que o segundo quadro anuncia um novo root bridge com ID `32768.00:11:22:33:44:66` e
   que a porta 0x8001 entra em estado blocking.
4. Ajustar o formato solicitado: `CECYBER{root_32768_001122334466}`.
5. Enviar para `/verify` em um POST com JSON `{"flag": "CECYBER{root_32768_001122334466}"}` para
   receber a flag definitiva.

## Justificativa da pontuação
O desafio demanda conhecimentos básicos de STP e familiaridade com análise de PCAP,
mas fornece materiais completos. Pontuação sugerida: 120 pontos.

## Flag
`CECYBER{root_32768_001122334466}` — somente esta variação é aceita.
