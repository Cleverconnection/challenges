# Solução — Root Bridge Live

## Estratégia
A API emula uma sessão de reconvergência documentada pela equipe de Radia Perlman. A análise
passa por identificar em qual ponto o root bridge foi trocado e qual evento confirma o bloqueio
da porta redundante.

## Passos sugeridos
1. Consultar `GET /timeline` e localizar a entrada "Root takeover" com o MAC vencedor.
2. Confirmar no evento seguinte que a porta oposta do antigo root foi bloqueada.
3. Enviar `{"flag": "CTF{root_change_detected}"}` para `POST /verify`.

## Resultado
O endpoint retorna `{"flag": "CTF{root_change_detected}"}` apenas quando a resposta coincide
com a tomada de controle documentada, garantindo a unicidade da solução.
