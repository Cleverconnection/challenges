# Cabeçalhos Reveladores

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Cabeçalhos Reveladores | `CTF{headers_tell_secrets}` | Fácil |

## Execução
1. Um healthcheck de diagnóstico retorna cabeçalhos verbosos com caminhos internos e pistas sobre o ambiente. Esses indícios apontam para recursos acessíveis no próprio serviço.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Usar as pistas dos cabeçalhos para localizar o recurso protegido e obter a flag.
4. `CTF{headers_tell_secrets}`
5. Leia os cabeçalhos `X-*` e siga o caminho indicado para o arquivo de dica.

## Narrativa
Explorar Cabeçalhos Reveladores revela a flag quando a vulnerabilidade principal é compreendida e explorada.
