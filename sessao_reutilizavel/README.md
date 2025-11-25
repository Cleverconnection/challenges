# Sessão Reutilizável

## Visão geral
**Categoria:** Web

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Sessão Reutilizável | `CTF{weak_passwords_ruin_security}` | Fácil |

## Execução
1. Uma aplicação legada continua em produção para dar suporte a funcionalidades internas críticas. O portal de administração é usado para emitir tokens de sessão que habilitam processos automatizados e integrações entre sistemas, mas credenciais padrão e senhas triviais ainda estão válidas. O mecanismo de emissão também não valida entradas nem bloqueia tentativas falhas.
2. URL de acesso individual fornecida ao iniciar a instância do desafio.
3. Encontrar credenciais válidas explorando senhas fracas, recuperar o token interno e utilizá-lo para acessar recursos protegidos e obter a flag.
4. `CTF{weak_passwords_ruin_security}`
5. O token de login não é a flag; utilize-o no endpoint indicado pela aplicação para avançar.

## Narrativa
Explorar Sessão Reutilizável revela a flag quando a vulnerabilidade principal é compreendida e explorada.
