# Quebrando a Arquitetura

## Visão geral
Um painel modular permite que Trinity carregue páginas diretas do disco, registre eventos e valide integridade com a
mesma chave simétrica. A combinação de falhas expõe o segredo final.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Quebrando a Arquitetura | `CTF{Trinity_Arquitetura_Liberada}` | Difícil |

## Execução
1. Porta: 8084; Inclusão de arquivos com `pagina=...` (vulnerável a travessia); Registro editável via `/registrar`; Flag liberada por HMAC correto lido em `/flag`
2. Leia páginas fora do diretório, capture a chave reutilizada, envenene o log com o HMAC correto e destrave a mensagem.

## Narrativa
> "Eu não temo o caminho. Temo ficar parada." — Trinity avança, ainda que o sistema esteja com falhas graves.

Explorar Quebrando a Arquitetura revela a flag quando a vulnerabilidade principal é compreendida e explorada.
