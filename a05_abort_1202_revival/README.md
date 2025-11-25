# A05 — Abort 1202 Revival

## Visão geral
Simulação inspirada no famoso alarme 1202 da Apollo 11. Um núcleo em C com threads POSIX representa interrupções do computador de bordo, enquanto um controlador em Python injeta prioridades lidas de `config/prioridades.json`. Valores inadequados causam o retorno `ABORT 1202` e mantêm a missão em risco.

## Tabela de referência interna

| Desafio | Flag | Pontuação |
| ------- | ----- | --------- |
| Abort 1202 Revival | `CTF{abort_1202_superado}` | 25 |

## Execução
1. Iniciar o container para que o controlador rode continuamente.
2. Acompanhar `/var/log/navegadora/abort1202.log` para entender as prioridades ativas.
3. Ajustar o JSON de configuração para reduzir `prioridade_nav`, ajustar `prioridade_interface` e diminuir `carga_interruptores`.
4. Quando o núcleo executar sem disparar o alarme, a flag aparecerá na saída e no log.

## Narrativa
> "Nunca deixem que uma interrupção inesperada derrube o sistema." — Margaret Hamilton

Somente após garantir prioridade absoluta ao módulo de navegação o alarme é silenciado e o núcleo retorna o código de sucesso com a flag.
