# Solução — Correspondência pHash

## Análise
O backend possui um dicionário `CATALOGO` com três imagens e seus pHash. A rota `/comparar` calcula a
quantidade de bits diferentes (distância de Hamming) entre o hash enviado e cada valor do catálogo.

## Passo a passo
1. Requisite `GET /catalogo` para visualizar as entradas.
2. Envie `POST /comparar` com `{"phash": "abcdef1234567890"}`.
3. A resposta indica que `inaauguracao_imagenet.png` possui distância zero e inclui `"flag": "CTF{fei_fei_phash_match}"`.

## Flag
- `CTF{fei_fei_phash_match}`

## Observações
- A flag pode ser redefinida via variável de ambiente `FLAG`.
