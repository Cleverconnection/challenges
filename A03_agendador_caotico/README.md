# A03 — Agendador Caótico

## Visão geral
O scheduler da Navegadora Lunar está atribuindo prioridades incorretas, fazendo com que `NAV_CONTROL` seja executada tarde demais. O participante precisa ajustar `config/tarefas.yaml` para garantir que a tarefa crítica lidere a fila.

## Tabela de referência interna

| Desafio | Flag | Pontuação |
| ------- | ----- | --------- |
| Agendador Caótico | `CTF{prioridades_em_orbita}` | 10 |

## Execução
1. Iniciar o processo do agendador.
2. Observar os avisos no log `/var/log/navegadora/scheduler.log`.
3. Ajustar a prioridade de `NAV_CONTROL` para liderar a fila.

## Narrativa
> "O menor descuido de prioridade pode custar a missão inteira." — Margaret Hamilton

Quando `NAV_CONTROL` é promovida corretamente, o sistema confirma a restauração e exibe a flag.
