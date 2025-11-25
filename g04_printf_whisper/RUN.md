# Execução do serviço G04 — Printf Whisper

```bash
mkdir -p build
gcc -Wall -Wextra -O0 -fno-stack-protector -no-pie -o build/printf_whisper src/printf_whisper.c
socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./build/printf_whisper
```

Conecte-se com:

```bash
nc 127.0.0.1 1337
```

Envie payloads como `%p %p %p %p %s` para vasculhar a memória até revelar a flag.
