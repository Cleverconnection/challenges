# Timing Attack

## Visão geral
A API de login compara senha caractere por caractere e insere um atraso a cada caractere correto. Isso permite inferir a senha por medição de tempo, além de confirmar se o usuário existe.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Timing Attack | `CTF{timing_leak_username}` | Médio |

## Execução
1. Medir tempos de resposta para deduzir strings protegidas.; Automatizar brute force baseado em timing.; Entender a importância de comparações em tempo constante.
2. `POST /api/login` — Recebe `username` e `password`, retornando flag ao acertar `executivo`/`9246`.; `GET /` — Interface explicativa.
3. Suba o container. 2. Utilize scripts que enviem tentativas de senha medindo o tempo (por exemplo, `time.perf_counter()` em Python). 3. Determine o usuário correto e descubra a senha um caractere por vez.
4. Note que o usuário válido é `executivo`.; Medindo o tempo, identifique que cada caractere correto adiciona ~120ms. Descubra `9246`.; Envie `POST /api/login` com as credenciais corretas para obter a flag.

## Narrativa
Explorar Timing Attack revela a flag quando a vulnerabilidade principal é compreendida e explorada.
