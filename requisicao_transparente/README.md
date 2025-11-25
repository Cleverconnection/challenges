# Requisição Transparente

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Requisição Transparente | `CTF{ssrf_proxy_to_flag}` | Fácil |

## Execução
1. Um proxy de integrações busca conteúdo externo a partir de uma URL informada. Sem restrições de destino, o serviço pode ser induzido a consultar endereços internos da infraestrutura.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Explorar o proxy para alcançar um endpoint interno protegido e obter a flag.
4. `CTF{ssrf_proxy_to_flag}`
5. Aponte o proxy para 127.0.0.1/localhost e portas não públicas.

## Narrativa
Explorar Requisição Transparente revela a flag quando a vulnerabilidade principal é compreendida e explorada.
