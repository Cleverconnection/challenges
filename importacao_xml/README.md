# Importação XML

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Importação XML | `CTF{xxe_into_core}` | Fácil |

## Execução
1. Um importador XML processa documentos enviados com suporte a entidades externas. Arquivos locais do ambiente podem ser referenciados a partir do próprio XML.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Construir um documento XML que exponha um segredo utilizado para liberar a flag.
4. `CTF{xxe_into_core}`
5. Construa um `DOCTYPE` com `SYSTEM file:///` apontando para um arquivo útil.

## Narrativa
Explorar Importação XML revela a flag quando a vulnerabilidade principal é compreendida e explorada.
