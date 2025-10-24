# T3 — Eco do Oráculo

Para decifrar sinais, Trinity criou um painel de envio de arquivos. Toda submissão gera registros públicos com metadados
que podem revelar detalhes não previstos. Os operadores esqueceram de higienizar o log e ele expõe o segredo.

## Serviço

- Porta: 8082
- Recebe arquivos e cria registro textual com metadados
- Registro disponível em `/registros`

## Narrativa

> "A resposta está lá fora, Neo. Procure-a." — Trinity confia no Oráculo, mas sabe que curiosidade expõe demais.

Faça um envio qualquer e observe os registros. O segredo já estava lá, esperando para ser lido.
