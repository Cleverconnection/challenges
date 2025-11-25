# Legacy Logger

## Visão geral
No auditório lilás do laboratório de Grace Hopper, uma ferramenta web preserva registros históricos. A comandante dizia: "A linguagem mais poderosa é aquela que qualquer pessoa consegue ler". Contudo, arquivos enviados ao sistema ainda chegam em um dialeto cifrado. Sua missão é traduzir o log e resgatar a homenagem escondida.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Legacy Logger | `CTF{grace_rot_traducao}` | Fácil |

## Execução
1. Faça upload de um arquivo de log no serviço Flask (`app/main.py`). O backend identifica linhas iniciadas com `mensagem:` e aplica automaticamente uma transformação ROT13. Entenda a lógica, replique o processo localmente e descubra a flag escondida nos dados em `data/registro_legacy.txt`.
2. Aplicação Flask com três páginas temáticas em tons de roxo.; Arquivo de exemplo em `data/registro_legacy.txt` contendo a mensagem codificada.; Dependências listadas em `requirements.txt`.
3. Nenhuma imagem local binária é incluída: os templates referenciam acervos públicos em HTTPS.; Execute a aplicação com `flask --app app.main run --host 0.0.0.0 --port 8002`.

## Narrativa
Explorar Legacy Logger revela a flag quando a vulnerabilidade principal é compreendida e explorada.
