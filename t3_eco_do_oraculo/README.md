# Eco do Oráculo

## Visão geral
Para decifrar sinais, Trinity criou um painel de envio de arquivos. Toda submissão gera registros públicos com metadados
que podem revelar detalhes não previstos. Os operadores esqueceram de higienizar o log e ele expõe o segredo.

## Tabela de referência interna

| Desafio | Flag | Dificuldade |
| ------- | ----- | --------- |
| Eco do Oráculo | `CTF{Trinity_Log_Do_Oraculo}` | Fácil |

## Execução
1. Porta: 8082; Recebe arquivos e cria registro textual com metadados; Registro disponível em `/registros`
2. Faça um envio qualquer e observe os registros. O segredo já estava lá, esperando para ser lido.

## Narrativa
> "A resposta está lá fora, Neo. Procure-a." — Trinity confia no Oráculo, mas sabe que curiosidade expõe demais.

Explorar Eco do Oráculo revela a flag quando a vulnerabilidade principal é compreendida e explorada.
