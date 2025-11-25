# Chave Persistente

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Chave Persistente | `CTF{jwt_without_expiration}` | Fácil |

## Execução
1. Uma API interna emite tokens JWT para aplicações de backoffice sem expiração adequada e com validações permissivas no payload. Tokens antigos continuam aceitos e campos de função influenciam privilégios de acesso.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Obter um token válido, ajustar o payload para elevar privilégios e acessar o recurso protegido que expõe a flag.
4. `CTF{jwt_without_expiration}`
5. Inspecione o token e o payload; há um campo de função sem expiração para explorar.

## Narrativa
Explorar Chave Persistente revela a flag quando a vulnerabilidade principal é compreendida e explorada.
