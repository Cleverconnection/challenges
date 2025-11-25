# Manual Público

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Manual Público | `CTF{swagger_spill}` | Fácil |

## Execução
1. A documentação interativa da API foi publicada com exemplos que incluem chaves reais e rotas internas esquecidas. A interface permite executar chamadas diretamente.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Extrair dos exemplos a informação necessária para autenticar e obter a flag na rota apropriada.
4. `CTF{swagger_spill}`
5. Abra o `swagger.json` e verifique valores `example` em chaves de autenticação.

## Narrativa
Explorar Manual Público revela a flag quando a vulnerabilidade principal é compreendida e explorada.
