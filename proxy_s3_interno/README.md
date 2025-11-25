# Proxy S3 Interno

## Visão geral
Um proxy corporativo deveria permitir apenas URLs externas, mas aceita qualquer destino HTTP/HTTPS. Isso possibilita atingir um endpoint S3 interno que só autoriza acessos originados da própria máquina, expondo relatórios com a flag.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Proxy S3 Interno | `CTF{ssrf_s3_traversal}` | Médio |

## Execução
1. Construir SSRF para atingir serviços locais expostos pela aplicação.; Entender como endpoints de armazenamento simulam ACLs baseadas em IP.; Manipular parâmetros de consulta para ajustar cabeçalhos opcionais.
2. `GET /api/proxy?url=` — Proxy inseguro utilizado pelo workflow.; `GET /s3/internal/` — Simulação de bucket S3 com controle por IP (somente localhost).; `GET /` — Interface com instruções no tema Vivo.
3. Suba o container. 2. Teste `/api/proxy?url=http://example.com` para entender o formato de resposta. 3. Troque a URL para um endereço local.
4. Faça requisição a `/api/proxy?url=http://127.0.0.1:8080/s3/internal/statements/report.txt`.; O proxy buscará o objeto localmente e retornará o conteúdo com a flag.

## Narrativa
Explorar Proxy S3 Interno revela a flag quando a vulnerabilidade principal é compreendida e explorada.
