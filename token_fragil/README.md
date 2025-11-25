# Token Frágil

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Token Frágil | `CTF{weak_crypto_modes}` | Fácil |

## Execução
1. Tokens internos são cifrados em modo de bloco sem aleatoriedade adequada, permitindo recombinar pedaços para alterar o perfil de acesso sem conhecer a chave.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Construir um token aceito como privilegiado e obter a flag.
4. `CTF{weak_crypto_modes}`
5. Alinhe campos sensíveis em limites de bloco e faça cut-and-paste.

## Narrativa
Explorar Token Frágil revela a flag quando a vulnerabilidade principal é compreendida e explorada.
