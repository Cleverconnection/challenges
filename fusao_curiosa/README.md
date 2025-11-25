# Fusão Curiosa

## Visão geral
O processo de fusão de contas retorna tanto o registro primário atualizado quanto o registro secundário anexado. A conta VIP (`7777`) contém a flag nos campos de notas e acaba sendo devolvida ao cliente durante a fusão.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Fusão Curiosa | `CTF{account_merge_disclosure}` | Médio |

## Execução
1. Avaliar respostas de APIs que retornam objetos complexos após operações.; Explorar vazamentos decorrentes de junção de dados sensíveis.; Compreender como copiar dados inadvertidamente entre contas.
2. `GET /api/accounts` — Lista contas com dados públicos.; `POST /api/merge` — Realiza fusão entre duas contas.; `GET /flag` — Bloqueado; a flag só aparece via resposta do merge.
3. Suba o container do desafio. 2. Consulte `/api/accounts` para identificar IDs disponíveis. 3. Realize `POST /api/merge` definindo `primary` como uma conta comum (ex.: `1001`) e `secondary` como `7777`.
4. A resposta do merge inclui `"secondary": {"notes": "CTF{...}"}`. Basta ler o JSON retornado.

## Narrativa
Explorar Fusão Curiosa revela a flag quando a vulnerabilidade principal é compreendida e explorada.
