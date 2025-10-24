# Compilação do desafio G03 — Symbolic Pointer

```bash
mkdir -p build
gcc -Wall -g -O1 -o build/symbolic_pointer src/symbolic_pointer.c
```

A flag fica acessível na tabela de símbolos pública. Use `nm build/symbolic_pointer | grep memorial_grace` para localizar o endereço e extraia a string com `gdb` ou `python` lendo a seção `.rodata`.
