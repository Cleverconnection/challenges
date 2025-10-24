# WRITEUP — G02 Legacy Logger

## Visão geral
A aplicação Flask aceita upload de arquivos, percorre cada linha e aplica ROT13 quando encontra o prefixo `mensagem:`. O arquivo `data/registro_legacy.txt` contém a flag nessa forma.

## Passos de solução
1. Ler o arquivo de exemplo: `cat data/registro_legacy.txt`.
2. Aplicar ROT13 apenas à parte após `mensagem:`. Exemplo em Python:
   ```python
   import codecs

   with open("data/registro_legacy.txt", "r", encoding="utf-8") as handler:
       for line in handler:
           if line.startswith("mensagem:"):
               prefix, texto = line.split(":", 1)
               decodificado = codecs.decode(texto.strip(), "rot13")
               print(decodificado)
   ```
3. A saída imprime `CTF{grace_rot_traducao}`.

## Flag
`CTF{grace_rot_traducao}`
