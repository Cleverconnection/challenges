# Atlas de Visão

Fei-Fei Li liderou o ImageNet, projeto que catalisou a revolução do deep learning. O laboratório lhe concede acesso
à API de anotações usada para reconstruir a tag histórica da primeira versão pública do dataset.

## Acesso ao serviço

- Aplicação Flask escutando na porta `8080`.
- Endpoints úteis:
  - `GET /dataset` entrega segmentos com palavras-chave; agrupe-as para formar a etiqueta principal.
  - `GET /annotations` mostra tags de apoio utilizadas pelos pesquisadores.
  - `POST /vision` aceita um JSON com a lista `{"tags": [...]}`. Inclua a etiqueta correta em letras maiúsculas.
- Use utilitários como `curl` ou `python -m http.client` para enviar o POST final. Exemplo:
  ```bash
  curl -X POST "$URL/vision" -H 'Content-Type: application/json' -d '{"tags":["IMAGENET-2009"]}'
  ```

## Flag

O serviço retorna a flag no formato `CTF{...}` quando a lista enviada contém a etiqueta montada.
