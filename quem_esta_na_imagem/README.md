# Quem está na imagem?

## Visão geral
Fei-Fei Li sempre lembrou que “precisamos fazer com que a IA veja o mundo como nós o vemos”. Nesta galeria azul,
você interage com um painel que relembra a construção do ImageNet e o esforço coletivo de rotuladores humanos.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Quem está na imagem? | `CTF{fei_fei_memoria_azul}` | – |

## Execução
1. A aplicação Flask serve uma pequena galeria de imagens com três cenas coloridas. Uma das rotas (`/processar`) realiza uma análise simples: verifica qual cor é dominante em cada imagem (azul, verde ou vermelho) e combina esse resultado com as memórias de Fei-Fei para revelar a flag. Faça uma requisição `POST` com o identificador da imagem correta e recupere o segredo.
2. Código-fonte em Python (`app.py`) que simula a análise de dominância de cor.; Três imagens PNG fictícias armazenadas em `static/img`. Elas são representações simbólicas em tons de azul, verde e vermelho.; Arquivo `processar.py` (opcional) mostrando como automatizar a requisição.
3. Execute com `flask --app app.py run --host 0.0.0.0 --port 5006`.; Não há necessidade de fazer upload: os nomes das imagens são `luz_azul.png`, `floresta_verde.png`, `por_do_sol.png`.; A interface cita a frase “Imagens são mais do que pixels, são histórias sobre pessoas” – reproduzindo a visão de Fei-Fei.

## Narrativa
Explorar Quem está na imagem? revela a flag quando a vulnerabilidade principal é compreendida e explorada.
