# WRITEUP — G03 Symbolic Pointer

## Visão geral
O binário gerado preserva símbolos. O vetor `memorial_grace` armazena a flag como string global.

## Passos de solução
1. Compilar: `gcc -Wall -g -O1 -o build/symbolic_pointer src/symbolic_pointer.c`.
2. Listar símbolos: `nm -C build/symbolic_pointer | grep memorial` mostra a entrada `U memorial_grace` com o endereço.
3. Extração: abrir o binário em `gdb`, executar `x/s memorial_grace` ou usar `strings -n 10 build/symbolic_pointer | grep CTF`.
4. Resultado: `CTF{grace_symbol_legivel}`.

## Flag
`CTF{grace_symbol_legivel}`
