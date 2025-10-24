# G05 — Compiler's Shadow

## Narrativa
Na câmara roxa onde Hopper experimentava otimizações, um protótipo de analisador aceita comandos secretos. Para protegê-lo, a equipe implementou verificações antidebug e uma máquina de estados inspirada em compiladores. Apenas quem entende o fluxo consegue recuperar a mensagem final.

## Objetivo
Compile `src/compilers_shadow.c` com as otimizações sugeridas, interaja com o binário via terminal ou exponha-o em um serviço TCP e supere:
1. A checagem contra depuração (`ptrace`).
2. A máquina de estados que espera três comandos específicos na ordem correta.
3. O desafio lógico que calcula um token numérico baseado na soma dos caracteres.

Ao concluir, o programa decodifica a flag `CTF{...}` armazenada com múltiplas transformações.

## Recursos fornecidos
- Código C com anti-debug, máquina de estados e decodificador com rotor.
- Orientações de compilação e execução em `BUILD.md`.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Compiler's Shadow | CTF{grace_shadow_otimizacao} | Engenharia reversa com anti-debug |

## Observações
- Para expor via TCP, combine o binário com `socat` semelhante ao desafio G04.
- Inclua o parâmetro `-O2` para que o fluxo de controle gere código mais compacto, simulando binário otimizado.
