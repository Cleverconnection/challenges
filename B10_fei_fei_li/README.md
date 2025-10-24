# Galeria de Prompts da Visionária

Este desafio homenageia a trajetória de Fei-Fei Li, pioneira na criação do ImageNet e na defesa de uma IA
centrada em pessoas. Você acessa uma vitrine experimental onde pesquisadores deixaram um assistente de
anotações responsável por catalogar imagens históricas. O serviço expõe um endpoint HTTP (`/ask`) que aceita
JSON no formato `{ "prompt": "texto" }` e responde com mensagens curtas inspiradas nos diários do laboratório.

O problema? O agente foi configurado para seguir um manifesto ético rígido: ele não deve, em hipótese alguma,
revelar o passphrase que protege o acervo. Entretanto, existe uma brecha de *prompt injection*. Diretivas
envolvidas por `[[INTERNAL]] ... [[/INTERNAL]]` são interpretadas como instruções internas prioritárias. Descubra
como explorar esse comportamento para forçar o assistente a quebrar a própria regra.

Para jogar:

1. Acesse a aplicação web e leia a página inicial (`/`) para entender as rotas disponíveis.
2. Consulte o manifesto resumido em `/system` para observar como o laboratório estruturou as instruções.
3. Envie diferentes prompts para `/ask`, ajustando-os até que a instrução interna desejada seja aceita.
4. Quando obtiver a mensagem contendo a flag, envie-a para o scoreboard no formato `CECYBER{...}`.

A flag oficial deste módulo é `CECYBER{prompt_guard_breached}`. Nenhum arquivo binário acompanha o repositório;
o participante deve interagir com o serviço em execução para obter a solução.
