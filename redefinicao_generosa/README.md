# Redefinição Generosa

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Redefinição Generosa | `CTF{reset_enum_abuse}` | Fácil |

## Execução
1. Um fluxo de redefinição aceita identificadores numéricos e retorna links de reset sem validar a posse da conta. IDs previsíveis permitem descobrir usuários privilegiados.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Enumerar identificadores até obter um link de reset privilegiado e usá-lo para alcançar a flag.
4. `CTF{reset_enum_abuse}`
5. Observe mensagens distintas para IDs existentes vs. inexistentes e siga o link de reset.

## Narrativa
Explorar Redefinição Generosa revela a flag quando a vulnerabilidade principal é compreendida e explorada.
