# G04 — Printf Whisper

## Narrativa
No convés lilás da embarcação de Grace Hopper, uma cadete configurou um serviço que ecoa mensagens usando `printf`. A almirante alertou: "O perigo está nas suposições não verificadas". O serviço deixou escapar uma vulnerabilidade clássica.

## Objetivo
Compile `src/printf_whisper.c` com proteções mínimas e exponha-o via `socat` ou `nc -lk`. Explore o serviço enviando sequências de formato (`%p`, `%x`, `%s`) até vazar a flag armazenada na memória.

## Recursos fornecidos
- Código C com vulnerabilidade de format string.
- Script `RUN.md` sugerindo como expor o binário via TCP.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Printf Whisper | CTF{grace_printf_confiança} | Exploração de format string |

## Observações
- Compile sem PIE e com `-no-pie -fno-stack-protector` para simplificar o vazamento.
- O texto inicial cita a famosa frase: "A linguagem mais poderosa é aquela que qualquer pessoa consegue ler".
