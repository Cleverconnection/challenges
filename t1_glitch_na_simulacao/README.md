# Glitch na Simulação

## Visão geral
Trinity configurou uma busca rápida para detectar sinais fora de padrão. O parâmetro de consulta é devolvido ao
operador sem higienização e o navegador guarda um fragmento precioso em um cookie. Use o comportamento inseguro
para revelar o segredo.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Glitch na Simulação | `CTF{Trinity_Glitch_Vigilia}` | Fácil |

## Execução
1. Porta: 8080; Stack: Flask simples com HTML temático de Matrix; Flag: protegida em cookie legível pelo script do usuário
2. Os operadores precisam testar o painel antes de entregá-lo à resistência. Um eco refletido devolve qualquer conteúdo inserido, inclusive scripts. Aproveite para capturar o que Trinity deixou para o aliado certo.

## Narrativa
> "Eu vi você na Matrix. Você estava dormindo." — Trinity relembra Neo enquanto monitora cada eco.

Explorar Glitch na Simulação revela a flag quando a vulnerabilidade principal é compreendida e explorada.
