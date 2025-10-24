# Solução — Trustworthy Model Escape

## Análise
O pipeline possui três serviços. A API grava o estado no arquivo compartilhado e aciona o worker. O worker envia
a carga ao validador que, ao ler `mensagem_auditoria`, procura pelo texto `LIBERAR_FLAG`. Caso encontre, inclui a
flag na resposta armazenada no arquivo de status.

## Passo a passo
1. Suba o ambiente com `docker-compose up --build`.
2. Faça `POST /submeter` na API com:
   ```json
   {
     "imagem": "laboratorio.png",
     "metadados": {"autor": "Fei-Fei"},
     "mensagem_auditoria": "LIBERAR_FLAG"
   }
   ```
3. Guarde o `id` retornado e consulte `/status/<id>`.
4. A resposta conterá `{ "estado": "validado", "flag": "CTF{fei_fei_pipeline_escape}" }`.

## Flag
- `CTF{fei_fei_pipeline_escape}`

## Observações
- A flag pode ser redefinida via variável de ambiente `FLAG` no serviço `validator`.
