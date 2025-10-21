# Depuradora do Mark I — Write-up

## Resumo

O desafio apresenta uma API com duas rotas principais: `/console` e `/punchcard`. O log retornado pelo console
lista nove eventos, cada um com uma letra destacada no início da linha, formando "FLOWMATIC". O endpoint `/punchcard`
converte o parâmetro `opcode` em maiúsculas e compara com `SECRET_OPCODE = "FLOW-MATIC"`.

## Solução

1. Faça `GET /console` para capturar o log.
2. Leia as letras associadas às fitas (F, L, O, W, M, A, T, I, C) e monte a string `FLOW-MATIC`.
3. Execute `GET /punchcard?opcode=FLOW-MATIC`.
4. O serviço retorna `CTF{Flowmatic_Debug_Master}`.

## Dificuldade

Exige observação e reconstrução de uma palavra-chave com base em contexto histórico. Pouco código, mas envolve
interpretação — pontuação sugerida: 150 pontos.

## Flags Aceitas

- `CTF{Flowmatic_Debug_Master}` (default configurado no container).
- Variações personalizadas podem ser injetadas via variável de ambiente `FLAG`.
