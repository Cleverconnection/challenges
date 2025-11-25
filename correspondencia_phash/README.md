# G07 — Correspondência pHash

## Narrativa
Na sala azul do laboratório de Fei-Fei Li, uma coleção de imagens históricas foi arquivada. Cada fotografia
possui um hash perceptual (pHash) para identificar padrões visuais aproximados. O painel exibe uma lista de
hashes e informa que uma delas guarda uma mensagem oculta sobre o ImageNet.

## Objetivo
Use o endpoint `/comparar` para enviar um pHash no formato hexadecimal. O serviço compara a distância de Hamming
com as amostras armazenadas e retorna o nome da imagem mais próxima. Quando a correspondência for a foto da
inauguração do ImageNet, a flag será exibida.

## Recursos fornecidos
- Aplicação Flask (`app.py`) com rotas de catálogo e comparação.
- Dados estáticos com os pHash já calculados (valores fictícios).
- Página HTML com contexto histórico, incluindo a frase “A curiosidade é o combustível da visão computacional”.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Correspondência pHash | CTF{fei_fei_phash_match} | Hash perceptual e busca aproximada |

## Observações
- Execute o serviço com `flask --app app.py run --host 0.0.0.0 --port 5007`.
- O endpoint `/catalogo` retorna a lista de imagens e seus pHash.
- `/comparar` aceita um JSON com `{ "phash": "f3a5..." }` e devolve o par com menor distância.
