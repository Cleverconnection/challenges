# Compilação do desafio G01 — Hello, Compiler

Execute os comandos abaixo em um ambiente GNU/Linux com `gcc` instalado:

```bash
mkdir -p build
gcc -Wall -Wextra -O2 -fno-plt -o build/hello_compiler src/hello_compiler.c
```

Após gerar o binário, execute-o:

```bash
./build/hello_compiler
```

Use ferramentas como `objdump -s -j .rodata build/hello_compiler` ou `xxd build/hello_compiler` para localizar a sequência ofuscada e aplique o script `scripts/decoder.py` para revelar a flag.
