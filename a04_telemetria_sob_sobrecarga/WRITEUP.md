# Solução — A04 Telemetria Sob Sobrecarga

## Passo a passo
1. Abrir o site do desafio. As três páginas mostram alertas e referências às prioridades erradas.
2. Checar `/data/telemetry.log`: há linhas avisando que `NAV_SAFE` foi abortada por saturação.
3. Verificar `config/config.json`, cujo conteúdo inicial é:
   ```json
   {
     "modo": "DEGRADED",
     "prioridade_nav_control": 4,
     "prioridade_coleta_dados": 2
   }
   ```
4. Editar o arquivo para conceder prioridade máxima a `NAV_SAFE` e sinalizar o modo correto. Um exemplo funcional:
   ```json
   {
     "modo": "SAFE_FLIGHT",
     "prioridade_nav_control": 0,
     "prioridade_coleta_dados": 3
   }
   ```
5. Salvar. O monitor detecta a alteração e escreve no log:
   ```
   SAFE_FLIGHT restaurado. NAV_SAFE ativo com prioridade=0. Sinalização completa: CTF{telemetria_em_modo_safe}
   ```
6. A flag pode ser lida no log e a interface passa a exibir o modo correto.

## Lições
- Logs ricos auxiliam no diagnóstico sob carga.
- Prioridades de telemetria devem privilegiar a segurança da tripulação.
- O trabalho minucioso de Hamilton inspira o ajuste preventivo contra falhas.
