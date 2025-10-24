# Solução — Tree Guard

## Resumo
O arquivo `tree_guard_trace.txt` contém três linhas. As duas primeiras mostram o comportamento
legítimo do domínio STP; a última denuncia o atacante.

## Procedimento
1. Baixar o trace via `GET /trace`.
2. Notar que o terceiro registro apresenta `src=00:11:22:33:44:99` e `root=00:11:22:33:44:99`.
3. Concluir que o emissor está fingindo ser raiz ao copiar o próprio MAC para o campo de root ID.
4. Enviar `{"flag": "CTF{falsa_root_00:11:22:33:44:99}"}` para `POST /verify`.

## Validação
O serviço responde com a mesma flag `CTF{falsa_root_00:11:22:33:44:99}` apenas quando a justificativa
está correta, garantindo a pontuação.
