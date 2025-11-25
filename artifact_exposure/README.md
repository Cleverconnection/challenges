# Artifact Exposure

## Visão geral
O simulador de pipeline CI/CD publica artefatos gerados pela última execução em um diretório acessível. O arquivo `runner.log` contém informações operacionais e, por engano, um segredo sensível exposto pelo script de build.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Artifact Exposure | `CTF{supply_chain_artifact}` | Médio |

## Execução
1. Enumerar endpoints de distribuição de artefatos.; Baixar logs de execução para buscar segredos.; Compreender os riscos de exposição de pipelines e runners.
2. `GET /api/pipelines/latest` — Retorna metadados sobre a execução mais recente.; `GET /artifact/runner.log` — Disponibiliza o log com a flag embutida.; `GET /` — Painel com orientação ao analista.
3. Levante o container do desafio. 2. Consulte `/api/pipelines/latest` para descobrir o caminho do artefato. 3. Faça download do arquivo informado utilizando navegador ou `curl`.
4. Acesse diretamente `GET /artifact/runner.log` e leia a linha `Secret token`, que carrega a flag do desafio.

## Narrativa
Explorar Artifact Exposure revela a flag quando a vulnerabilidade principal é compreendida e explorada.
