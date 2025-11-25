# Porta 22 de Zion

## Visão geral
Trinity precisou abrir a porta 22 para manter contato com a nave. Fragmentos das credenciais ficaram em arquivos
públicos, permitindo reconstruir a senha e autenticar no serviço remoto.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Porta 22 de Zion | `CTF{Trinity_Zion_SSH}` | Difícil |

## Execução
1. Porta: 8083; Listagem de memórias públicas contendo fragmentos de senha; Endpoint `/ssh` que exige autenticação básica
2. Recolete cada pista, una os fragmentos na ordem indicada e acesse `/ssh` com a usuária revelada para recuperar a flag.

## Narrativa
> "Eu sabia que você viria." — Trinity separou pedaços da senha para que nenhum agente capturasse tudo de uma vez.

Explorar Porta 22 de Zion revela a flag quando a vulnerabilidade principal é compreendida e explorada.
