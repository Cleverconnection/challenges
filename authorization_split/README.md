# Authorization Split

## Visão geral
O serviço espera um cabeçalho `Authorization: Token token=;role=` e converte todas as partes em um dicionário minúsculo. Ao enviar o token válido e definir `role=admin`, o backend concede acesso completo.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Authorization Split | `CTF{auth_header_split}` | Médio |

## Execução
1. Inspecionar formatos personalizados de header Authorization.; Manipular múltiplos parâmetros em um único header.; Validar respostas diferenciadas conforme o role recebido.
2. `GET /` — Exibe o token padrão (`svc-ops-2025`).; `GET /api/secure` — Processa o header customizado e retorna a flag quando `role=admin`.
3. Suba o container. 2. Monte o header `Authorization: Token token=svc-ops-2025;role=admin`. 3. Faça a requisição via `curl` ou ferramenta de testes.
4. `curl -H "Authorization: Token token=svc-ops-2025;role=admin" http://localhost:8080/api/secure`; A resposta JSON incluirá a flag no campo `flag`.

## Narrativa
Explorar Authorization Split revela a flag quando a vulnerabilidade principal é compreendida e explorada.
