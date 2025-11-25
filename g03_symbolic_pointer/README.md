# G03 — Symbolic Pointer

## Narrativa
Grace Hopper defendia nomes significativos em código: "Devemos escrever programas que possam ser lidos por humanos". Este exercício lilás entrega um código C onde símbolos públicos revelam o caminho para a flag.

## Objetivo
Compile `src/symbolic_pointer.c` e use ferramentas como `nm`, `readelf -s` ou `objdump -t` para inspecionar a tabela de símbolos. Identifique o símbolo que referencia a flag armazenada na memória e extraia a string.

## Recursos fornecidos
- Código C com símbolos descritivos.
- Instruções de compilação em `BUILD.md`.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Symbolic Pointer | CTF{grace_symbol_legivel} | Leitura de símbolos públicos |

## Observações
- Não distribua o binário gerado; este repositório apenas contém o código-fonte.
- As mensagens de execução citam a frase de Hopper sobre legibilidade.
