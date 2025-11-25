# Hello, Compiler

## Visão geral
Grace Hopper sempre lembrava que "a maneira mais perigosa de começar um projeto é dizer: sempre fizemos assim". Nesta oficina roxa dedicada à Dama dos Compiladores, você recebe o código-fonte de um executável simples que ecoa memórias dos primeiros compiladores A-0. Explore as seções de dados do programa para encontrar a lembrança que Hopper deixou escondida.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Hello, Compiler | `CTF{grace_xor_matematica}` | Fácil |

## Execução
1. Compile o código C fornecido em `src/hello_compiler.c`, analise a seção `.rodata` e desfaça a ofuscação XOR para recuperar a flag. A flag segue o padrão `CTF{...}`.
2. Código-fonte em C com rotina de impressão temática em tons lilás.; Script auxiliar em Python (`scripts/decoder.py`) que demonstra como automatizar a remoção do XOR.; Instruções de compilação no arquivo `BUILD.md`.
3. Nenhum binário é distribuído: gere o executável localmente para praticar o fluxo completo.; Evite executar o binário em ambientes não controlados.
4. Essa frase acompanha a saída do programa, incentivando você a navegar por seções de dados e compreender como compiladores guardam segredos.

## Narrativa
> "Um navio no porto está seguro, mas não é para isso que os navios foram feitos." — Grace Hopper

Explorar Hello, Compiler revela a flag quando a vulnerabilidade principal é compreendida e explorada.
