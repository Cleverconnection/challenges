# Config Leak

## Visão geral
Um endpoint de configuração pensado para uso interno expõe configurações de todos os ambientes, incluindo chaves e a flag no ambiente de produção.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Config Leak | `CTF{config_endpoint_leak}` | Médio |

## Execução
1. Enumerar ambientes suportados em APIs de configuração.; Reconhecer objetos com segredos aninhados.; Valorizar a segmentação de dados sensíveis por ambiente.
2. `GET /api/config/` — Retorna configurações para `dev`, `prod`, etc.; `GET /` — Interface descritiva.
3. Suba o serviço do desafio. 2. Consulte `/api/config/dev` para ver a estrutura retornada. 3. Troque o parâmetro para `prod`.
4. A resposta de `/api/config/prod` contém `config.secrets.flag` com o valor da flag.

## Narrativa
Explorar Config Leak revela a flag quando a vulnerabilidade principal é compreendida e explorada.
