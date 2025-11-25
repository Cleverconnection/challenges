# Symbolic Pointer

## Visão geral
Grace Hopper defendia nomes significativos em código: "Devemos escrever programas que possam ser lidos por humanos". Este exercício lilás entrega um código C onde símbolos públicos revelam o caminho para a flag.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Symbolic Pointer | `CTF{grace_symbol_legivel}` | Fácil |

## Execução
1. Compile `src/symbolic_pointer.c` e use ferramentas como `nm`, `readelf -s` ou `objdump -t` para inspecionar a tabela de símbolos. Identifique o símbolo que referencia a flag armazenada na memória e extraia a string.
2. Código C com símbolos descritivos.; Instruções de compilação em `BUILD.md`.
3. Não distribua o binário gerado; este repositório apenas contém o código-fonte.; As mensagens de execução citam a frase de Hopper sobre legibilidade.

## Narrativa
Explorar Symbolic Pointer revela a flag quando a vulnerabilidade principal é compreendida e explorada.
