# Supervisora do Apollo — Write-up

## Solução

O console oferece dois endpoints informativos. `/alarms` revela os códigos 1201 e 1202 associados ao módulo de
navegação. `/checklist` lista explicitamente as etapas necessárias, incluindo a string `PROG1201-OVERRIDE`. O
endpoint `/guidance` converte o parâmetro `program` para maiúsculas e compara com `SECRET_PROGRAM`.

## Passos

1. Consulte `GET /checklist` para encontrar a sequência recomendada.
2. Identifique que a terceira etapa contém o código exato `PROG1201-OVERRIDE`.
3. Faça `GET /guidance?program=PROG1201-OVERRIDE`.
4. Receba `CTF{Software_On_The_Moon}`.

## Dificuldade

O desafio reforça a leitura cuidadosa da checklist e o entendimento do histórico de Margaret Hamilton. Pontuação
sugerida: 170 pontos.

## Flags Aceitas

- `CTF{Software_On_The_Moon}` — padrão do container.
- Valor alternativo configurável via variável de ambiente `FLAG`.
