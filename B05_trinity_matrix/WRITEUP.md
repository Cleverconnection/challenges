# Trinity — Write-up Interno

## Contexto

O desafio replica a cena inicial de Matrix (1999) quando Trinity encontra Neo no clube. Ele descobre que Trinity é a
hacker que invadiu o banco de dados da Receita Federal (IRS), e se surpreende por ela ser mulher.

## Solução

1. Leia `GET /hints` (opcional) para receber pistas literais sobre a cena.
2. Pesquise ou reassista ao filme para confirmar que Trinity foi responsável por invadir a Receita.
3. Envie `POST /verify` com `{"answer": "Banco de Dados da Receita"}` (qualquer variação de caixa funciona).
4. O serviço retorna `CTF{Banco_de_Dados_da_Receita}`.

## Justificativa de Pontuação

Por ser um desafio OSINT/textual, a dificuldade está em lembrar a cena ou realizar pesquisa rápida. Classificado como
100 pontos.

## Flags Aceitas

- `CTF{Banco_de_Dados_da_Receita}` — padrão.
- Organizadores podem ajustar via variável de ambiente `FLAG`.
