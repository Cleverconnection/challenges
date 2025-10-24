# WRITEUP — G01 Hello, Compiler

## Visão geral
O programa exibe mensagens sobre a trajetória de Grace Hopper e calcula um checksum. Não há flag explícita; a dica menciona analisar a seção `.rodata`.

## Passos de solução
1. **Compilação:** `gcc -Wall -Wextra -O2 -fno-plt -o build/hello_compiler src/hello_compiler.c`.
2. **Inspeção das seções:** `objdump -s -j .rodata build/hello_compiler` revela uma sequência de bytes não imprimíveis.
3. **Entendimento:** o código mantém o vetor `flag_xor` e a chave `"HOP"`. Cada byte da flag é XOR com a chave cíclica.
4. **Decodificação:** criar script Python:
   ```python
   KEY = b"HOP"
   FLAG_XOR = [11, 27, 22, 51, 40, 34, 41, 44, 53, 23,
               55, 63, 58, 16, 61, 41, 59, 53, 37, 46,
               36, 33, 44, 49, 53]
   print(bytes(v ^ KEY[i % len(KEY)] for i, v in enumerate(FLAG_XOR)))
   ```
5. **Resultado:** a execução imprime `CTF{grace_xor_matematica}`.

## Flag
`CTF{grace_xor_matematica}`
