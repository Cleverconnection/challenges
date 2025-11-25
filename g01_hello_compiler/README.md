# G01 — Hello, Compiler

## Narrativa
Grace Hopper sempre lembrava que "a maneira mais perigosa de começar um projeto é dizer: sempre fizemos assim". Nesta oficina roxa dedicada à Dama dos Compiladores, você recebe o código-fonte de um executável simples que ecoa memórias dos primeiros compiladores A-0. Explore as seções de dados do programa para encontrar a lembrança que Hopper deixou escondida.

## Objetivo
Compile o código C fornecido em `src/hello_compiler.c`, analise a seção `.rodata` e desfaça a ofuscação XOR para recuperar a flag. A flag segue o padrão `CTF{...}`.

## Recursos fornecidos
- Código-fonte em C com rotina de impressão temática em tons lilás.
- Script auxiliar em Python (`scripts/decoder.py`) que demonstra como automatizar a remoção do XOR.
- Instruções de compilação no arquivo `BUILD.md`.

## Tabela de referência
| Desafio | Flag | Valor conceitual |
|---------|------|------------------|
| Hello, Compiler | CTF{grace_xor_matematica} | Interpretação de dados em executáveis |

## Observações
- Nenhum binário é distribuído: gere o executável localmente para praticar o fluxo completo.
- Evite executar o binário em ambientes não controlados.

## Contexto histórico
> "Um navio no porto está seguro, mas não é para isso que os navios foram feitos." — Grace Hopper

Essa frase acompanha a saída do programa, incentivando você a navegar por seções de dados e compreender como compiladores guardam segredos.
