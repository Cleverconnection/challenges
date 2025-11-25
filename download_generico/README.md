# Download Genérico

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Download Genérico | `CTF{file_download_traversal}` | Fácil |

## Execução
1. Um endpoint de download aceita caminhos arbitrários para localizar arquivos, permitindo fuga do diretório previsto e acesso indevido a artefatos internos.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Fornecer um caminho que conduza a um arquivo com token e usá-lo para obter a flag.
4. `CTF{file_download_traversal}`
5. Tente caminhos absolutos ou `../` para alcançar a pasta interna alvo.

## Narrativa
Explorar Download Genérico revela a flag quando a vulnerabilidade principal é compreendida e explorada.
