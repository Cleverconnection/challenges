# Correspondência pHash

## Visão geral
Na sala azul do laboratório de Fei-Fei Li, uma coleção de imagens históricas foi arquivada. Cada fotografia
possui um hash perceptual (pHash) para identificar padrões visuais aproximados. O painel exibe uma lista de
hashes e informa que uma delas guarda uma mensagem oculta sobre o ImageNet.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Correspondência pHash | `CTF{fei_fei_phash_match}` | Médio |

## Execução
1. Use o endpoint `/comparar` para enviar um pHash no formato hexadecimal. O serviço compara a distância de Hamming com as amostras armazenadas e retorna o nome da imagem mais próxima. Quando a correspondência for a foto da inauguração do ImageNet, a flag será exibida.
2. Aplicação Flask (`app.py`) com rotas de catálogo e comparação.; Dados estáticos com os pHash já calculados (valores fictícios).; Página HTML com contexto histórico, incluindo a frase “A curiosidade é o combustível da visão computacional”.
3. Execute o serviço com `flask --app app.py run --host 0.0.0.0 --port 5007`.; O endpoint `/catalogo` retorna a lista de imagens e seus pHash.; `/comparar` aceita um JSON com `{ "phash": "f3a5..." }` e devolve o par com menor distância.

## Narrativa
Explorar Correspondência pHash revela a flag quando a vulnerabilidade principal é compreendida e explorada.
