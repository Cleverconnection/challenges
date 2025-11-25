# T1 — Glitch na Simulação

Trinity configurou uma busca rápida para detectar sinais fora de padrão. O parâmetro de consulta é devolvido ao
operador sem higienização e o navegador guarda um fragmento precioso em um cookie. Use o comportamento inseguro
para revelar o segredo.

## Serviço

- Porta: 8080
- Stack: Flask simples com HTML temático de Matrix
- Flag: protegida em cookie legível pelo script do usuário

## Narrativa

> "Eu vi você na Matrix. Você estava dormindo." — Trinity relembra Neo enquanto monitora cada eco.

Os operadores precisam testar o painel antes de entregá-lo à resistência. Um eco refletido devolve qualquer
conteúdo inserido, inclusive scripts. Aproveite para capturar o que Trinity deixou para o aliado certo.
