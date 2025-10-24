# T5 — Quebrando a Arquitetura

Um painel modular permite que Trinity carregue páginas diretas do disco, registre eventos e valide integridade com a
mesma chave simétrica. A combinação de falhas expõe o segredo final.

## Serviço

- Porta: 8084
- Inclusão de arquivos com `pagina=...` (vulnerável a travessia)
- Registro editável via `/registrar`
- Flag liberada por HMAC correto lido em `/flag`

## Narrativa

> "Eu não temo o caminho. Temo ficar parada." — Trinity avança, ainda que o sistema esteja com falhas graves.

Leia páginas fora do diretório, capture a chave reutilizada, envenene o log com o HMAC correto e destrave a mensagem.
