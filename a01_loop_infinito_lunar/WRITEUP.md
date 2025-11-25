# Solução — A01 Loop Infinito Lunar

## Passo a passo
1. Ao iniciar a instância, verificar os registros em `/var/log/navegadora/loop.log`. Os avisos mostram que `sentinela=travado` e que o estado segue em `ORBITA_CAOTICA`.
2. Abrir o arquivo `config/controle_loop.json`. Ele contém:
   ```json
   {
     "sentinela_laco": "travado",
     "estado_atual": "ORBITA_CAOTICA"
   }
   ```
3. Editar os valores para liberar a sentinela e ajustar o estado crítico:
   ```json
   {
     "sentinela_laco": "LIBERADO",
     "estado_atual": "ORBITA_ESTAVEL"
   }
   ```
4. Salvar o arquivo e aguardar o próximo ciclo do processo. O log passa a registrar a sequência de correção e o programa imprime:
   ```
   Sequência de correção concluída com sucesso. Registro de missão autenticado: CTF{loop_infinito_corrigido}
   ```

## Lições
- Estados mal configurados impedem a conclusão de rotinas críticas.
- Logs bem escritos guiam o ajuste sem revelar diretamente a solução.
- A filosofia de Margaret Hamilton sobre prevenção total de falhas orienta a validação do processo.
