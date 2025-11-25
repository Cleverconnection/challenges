# Supervisora do Apollo

Margaret Hamilton tornou-se símbolo da engenharia de software ao garantir a segurança das missões Apollo. Neste
desafio você revisita o console de alarmes do Módulo Lunar para reativar o programa que ela sugeriu durante o
famoso incidente do erro 1201.

## Acesso ao serviço

- Aplicação Flask disponível na porta `8080`.
- Endpoints:
  - `GET /alarms` — mostra os alarmes ativos e seus módulos.
  - `GET /checklist` — lista a sequência de ações recomendadas por Hamilton.
  - `GET /guidance?program=...` — retorna a flag quando recebe o código correto, em caixa alta.
- Utilize `curl "$URL/guidance?program=PROG1201-OVERRIDE"` após interpretar a checklist.

## Flag

A flag é retornada no corpo da resposta em formato `CTF{...}`.
