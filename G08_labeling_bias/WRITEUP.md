# Solução — Viés de Rotulagem

## Análise
O arquivo `data/dataset.json` possui registros onde pessoas com `tom_de_pele` “escuro” recebem `atributo`
“neutro”. O endpoint `/corrigir` exige que essas entradas sejam ajustadas para “respeitado”.

## Passo a passo
1. Faça `GET /dados` para obter a lista original.
2. Altere cada registro com `tom_de_pele == "escuro"` para ter `atributo == "respeitado"`.
3. Envie `POST /corrigir` com `{ "registros": [...] }` contendo os ajustes.
4. O serviço responderá com `{"mensagem": "Viés corrigido", "flag": "CTF{fei_fei_bias_ajustado}"}`.

## Flag
- `CTF{fei_fei_bias_ajustado}`

## Observações
- O script `scripts/ajuste.py` ilustra a automatização.
- A flag pode ser modificada via variável de ambiente `FLAG`.
