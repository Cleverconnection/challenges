# Write-up — T5 Quebrando a Arquitetura

1. Acesse `/painel?pagina=boas_vindas.html` e observe a possibilidade de escolher outros arquivos.
2. Carregue `/painel?pagina=../segredos/chave.txt` para ler a chave `m0rf3u5_compartilha`.
3. Veja `/painel?pagina=manual.html` para confirmar a frase `ACESSO_ZION` e o formato `CHAVE=<hex>`.
4. Calcule `hmac_sha256("m0rf3u5_compartilha", "ACESSO_ZION")` obtendo `ec380caf5949426751791c4f591a3f982b158af981192a0873e50ee90baf492c`.
5. Envie `/registrar?entrada=CHAVE=ec380caf5949426751791c4f591a3f982b158af981192a0873e50ee90baf492c`.
6. Consulte `/flag` para receber `CTF{Trinity_Arquitetura_Liberada}`.
