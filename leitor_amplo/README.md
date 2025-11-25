# Leitor Amplo

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Leitor Amplo | `CTF{path_traversal_master}` | Fácil |

## Execução
1. Um leitor de arquivos serve documentos a partir de um diretório base do container. Devido à concatenação direta de caminhos, é possível acessar arquivos fora do diretório previsto.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Realizar travessia de diretórios para ler o arquivo de flag localizado fora da pasta pública.
4. `CTF{path_traversal_master}`
5. Teste sequências com `../` para sair do diretório exposto.

## Narrativa
Explorar Leitor Amplo revela a flag quando a vulnerabilidade principal é compreendida e explorada.
