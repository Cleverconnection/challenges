# Registros Não Confiáveis

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Registros Não Confiáveis | `CTF{logs_are_trust_issue}` | Fácil |

## Execução
1. Um painel operacional grava entradas do usuário diretamente em um arquivo de log. Sem sanitização, é possível injetar conteúdo tratado como evento válido por outros componentes.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Injetar uma marcação controlada no log e utilizá-la para satisfazer a verificação que libera a flag.
4. `CTF{logs_are_trust_issue}`
5. Envie uma entrada contendo um marcador `chave=valor` esperado pelo verificador.

## Narrativa
Explorar Registros Não Confiáveis revela a flag quando a vulnerabilidade principal é compreendida e explorada.
