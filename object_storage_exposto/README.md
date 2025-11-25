# Object Storage Exposto

## Visão geral
A API de download concatena o caminho solicitado diretamente ao diretório base e lê o arquivo resultante sem validar se está em `storage/public`. Isso permite acessar arquivos privados contendo a flag.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Object Storage Exposto | `CTF{object_storage_flag}` | Médio |

## Execução
1. Explorar exposições de armazenamento tipo object storage.; Entender os riscos de confiar em caminhos fornecidos pelo cliente.; Navegar por diretórios internos sem sanitização.
2. `GET /api/file?path=` — Retorna o conteúdo do arquivo solicitado.; Estrutura de diretórios `storage/public` e `storage/private`.
3. Inicie o container. 2. Solicite `GET /api/file?path=public/notice.txt` para testar o endpoint. 3. Modifique o parâmetro para acessar arquivos privados.
4. Requisite `GET /api/file?path=private/flag.txt`.; O JSON retornará o conteúdo do arquivo com a flag.

## Narrativa
Explorar Object Storage Exposto revela a flag quando a vulnerabilidade principal é compreendida e explorada.
