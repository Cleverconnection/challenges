# Transporte Opcional

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Transporte Opcional | `CTF{tls_redirect_missing}` | Fácil |

## Execução
1. Um serviço opera simultaneamente em HTTP e HTTPS sem forçar redirecionamento seguro. Sessões e dados podem transitar em claro quando acessados sem TLS.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Capturar informações de sessão acessando o serviço de forma não cifrada e utilizá-las para recuperar a flag.
4. `CTF{tls_redirect_missing}`
5. Acesse via HTTP simples e verifique cookies ou JSON de sessão.

## Narrativa
Explorar Transporte Opcional revela a flag quando a vulnerabilidade principal é compreendida e explorada.
