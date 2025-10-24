# G10 — Trustworthy Model Escape

## Narrativa
Fei-Fei Li participa de uma rede de serviços que garantem curadoria ética para modelos de visão. Um pipeline
multi-etapas recebe requisições no API Gateway, encaminha para uma fila processada por trabalhadores e, por fim,
um validador criptográfico libera chaves. Há, porém, uma brecha: um campo mal filtrado permite inserir uma
"mensagem de auditoria" que contamina a entrada do validador.

## Objetivo
1. Interaja com a API (`/submeter`) enviando um JSON com `imagem`, `metadados` e `mensagem_auditoria`.
2. O API Gateway repassa a mensagem para o `worker`, que a anexa à carga enviada ao `validator`.
3. Se a `mensagem_auditoria` contiver `LIBERAR_FLAG`, o validador retorna a chave `CTF{...}`.
4. Recolha a resposta final em `/status/<id>`.

## Recursos fornecidos
- Docker Compose com três serviços: `api`, `worker`, `validator`.
- Código Python de cada camada na pasta `services/`.
- Interface HTML azul para visualizar o diagrama do pipeline.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Trustworthy Model Escape | CTF{fei_fei_pipeline_escape} | Segurança em cadeias de serviços | 

## Observações
- Inicie com `docker-compose up --build` dentro da pasta do desafio.
- Use `POST /submeter` com um JSON semelhante a `{ "imagem": "laboratorio.png", "mensagem_auditoria": "LIBERAR_FLAG" }`.
- A resposta final em `/status/<id>` incluirá o campo `flag`.
