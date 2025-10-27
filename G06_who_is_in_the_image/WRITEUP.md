# Solução — Quem está na imagem?

## Análise
A galeria apresenta três imagens simbólicas: `luz_azul.png`, `floresta_verde.png` e `por_do_sol.png`. O backend
(arquivo `app.py`) possui um dicionário `CENAS` com a cor dominante de cada imagem. A rota `/processar` espera
um JSON com o campo `imagem`. Se a cor associada for `AZUL`, a flag é retornada.

## Passo a passo
1. Acesse a rota `/galeria` para entender a narrativa e identificar os nomes das imagens.
2. Faça uma requisição `POST` para `/processar` com `{"imagem": "luz_azul.png"}`.
3. A resposta conterá `{"mensagem": "Imagens são histórias sobre pessoas.", "flag": "CTF{fei_fei_memoria_azul}"}`.

## Flag
- `CTF{fei_fei_memoria_azul}`

## Dicas para homologação
- A flag pode ser personalizada via variável de ambiente `FLAG`.
- As páginas HTML estão em tons de azul e usam citações reais de Fei-Fei Li.
