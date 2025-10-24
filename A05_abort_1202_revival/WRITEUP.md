# Solução — A05 Abort 1202 Revival

## Passo a passo
1. Verificar `/var/log/navegadora/abort1202.log`. O controlador informa repetidamente que o núcleo encerrou com código 1202.
2. Abrir `config/prioridades.json` para observar os valores iniciais:
   ```json
   {
     "prioridade_nav": 4,
     "prioridade_interface": 3,
     "carga_interruptores": 120
   }
   ```
3. Ajustar o arquivo priorizando o módulo de navegação e reduzindo a carga de interrupções. Exemplo funcional:
   ```json
   {
     "prioridade_nav": 1,
     "prioridade_interface": 3,
     "carga_interruptores": 60
   }
   ```
   Qualquer combinação com `prioridade_nav` menor ou igual a `prioridade_interface` e menor ou igual a `2`, além de `carga_interruptores` abaixo de `80`, satisfaz o núcleo.
4. Salvar o arquivo. No próximo ciclo, o núcleo imprime:
   ```
   Resumo: NAV=1 DSKY=3 BURST=60
   CTF{abort_1202_superado}
   ```
5. O controlador escreve no log que o alarme foi contido e a flag é retornada ao terminal.

## Lições
- Controlar interrupções evita alarmes críticos semelhantes ao 1202 real.
- A combinação de C (núcleo) e Python (supervisão) reforça a importância de camadas cooperando.
- Planejamento de prioridades é um dos legados mais marcantes de Margaret Hamilton.
