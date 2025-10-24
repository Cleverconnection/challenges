# WRITEUP — G05 Compiler's Shadow

## Visão geral
O binário realiza uma checagem `ptrace` para dificultar depuração, exige comandos específicos e calcula um token a partir da palavra "FLOWMATIC". A flag está em `encoded_flag`, codificada por soma com rotor, rotação e XOR.

## Passos de solução
1. **Bypass do anti-debug:** execute sem debugger ou use `setarch -R`/patch para ignorar o retorno do `ptrace`. Como temos o código, basta rodar normalmente.
2. **Sequência de comandos:** a máquina de estados aceita apenas `iniciar compilador`, depois `executar a-0` e, por fim, `otimizar rotina`.
3. **Token numérico:** analisar `calcular_meta` revela um laço sobre "FLOWMATIC". Implementando em Python:
   ```python
   acumulador = 0x1F
   for c in b"FLOWMATIC":
       acumulador ^= c
       acumulador = ((acumulador << 3) | (acumulador >> 13)) & 0xFFFF
       acumulador += 7
   token = acumulador & 0xFFF  # 907
   ```
4. **Decodificação:** a função `girar_decodificador` soma o rotor, rotaciona à esquerda 1 bit e faz XOR com "HOPPER". Revertendo o processo obtemos `CTF{grace_shadow_otimizacao}`.

## Flag
`CTF{grace_shadow_otimizacao}`
