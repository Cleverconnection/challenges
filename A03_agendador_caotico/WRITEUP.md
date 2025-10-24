# Solução — A03 Agendador Caótico

## Passo a passo
1. Consultar `/var/log/navegadora/scheduler.log` e notar os avisos informando que `NAV_CONTROL` não lidera a fila.
2. Abrir `config/tarefas.yaml`. Inicialmente a prioridade de `NAV_CONTROL` é 5, mais alta que outras tarefas.
3. Ajustar para que `NAV_CONTROL` tenha a menor prioridade numérica:
   ```yaml
   tarefas:
     - nome: "NAV_CONTROL"
       prioridade: 0
     - nome: "COLETA_METEOROS"
       prioridade: 2
     - nome: "BALANCO_TERMICO"
       prioridade: 3
     - nome: "REGISTRO_CIENTIFICO"
       prioridade: 4
   ```
   (qualquer arranjo que mantenha `NAV_CONTROL` em primeiro lugar é aceito).
4. Salvar e aguardar. O log registra `NAV_CONTROL executada primeiro` e o programa imprime `NAV_CONTROL priorizada corretamente. CTF{prioridades_em_orbita}`.

## Lições
- Prioridades devem refletir criticidade das tarefas.
- Agendadores cooperativos são sensíveis à ordem de execução.
- Revisar tabelas de configuração é tão importante quanto revisar código fonte, como defendia Margaret Hamilton.
