# Compilação do desafio G05 — Compiler's Shadow

```bash
mkdir -p build
gcc -O2 -Wall -Wextra -fno-stack-protector -no-pie -o build/compilers_shadow src/compilers_shadow.c
```

Para simular o serviço remoto:

```bash
socat TCP-LISTEN:2222,reuseaddr,fork EXEC:./build/compilers_shadow
```

Conecte-se com `nc 127.0.0.1 2222` e siga a sequência descrita no README.
