# Solução — A02 Corrida pelo Controle

## Passo a passo
1. Examinar `/var/log/navegadora/corrida.log` e notar que as mensagens de alerta informam `Controle descompassado` com contagem de `Integridade_ok` baixa.
2. Abrir `config/controle_navegacao.json` para verificar o conteúdo inicial:
   ```json
   {
     "usar_trava": false
   }
   ```
3. Alterar o valor para `true`:
   ```json
   {
     "usar_trava": true
   }
   ```
4. Salvar e aguardar os próximos ciclos do serviço. O log começa a registrar linhas como `Estado sincronizado` e o processo imprime:
   ```
   Missão estabilizada sem condição de corrida. Registrando na cápsula: CTF{condicao_de_corrida_domada}
   ```

## Lições
- Sincronização com mutex impede inconsistência em variáveis compartilhadas.
- Logs claros direcionam a correção sem revelar a flag diretamente.
- Trabalhar com consciência de concorrência evita falhas semelhantes aos erros que a equipe de Margaret Hamilton antevia.
