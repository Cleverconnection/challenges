# Atlas de Visão — Write-up

## Descrição da Solução

A API fornece pistas diretas sobre a etiqueta esperada. O endpoint `/dataset` retorna palavras-chave divididas entre
os segmentos: `"IMA"`, `"GE"`, `"NET"` e `"-2009"`. Quando concatenadas, formam `IMAGENET-2009`. O endpoint
`/vision` espera um corpo JSON com a lista `tags` e normaliza cada item para letras maiúsculas, comparando com
`SECRET_TAG = "IMAGENET-2009"`.

## Passos

1. Solicite `GET /dataset` e identifique os fragmentos de texto.
2. Una os fragmentos para obter `IMAGENET-2009`.
3. Envie `POST /vision` com `{"tags":["IMAGENET-2009"]}`.
4. Receba a flag `CTF{Seeing_The_Unseen}` no campo `flag` da resposta JSON.

## Dificuldade

A tarefa exige interpretar pistas textuais e compreender o legado do ImageNet. Classificamos como nível intermediário
(200 pontos) por exigir um POST com JSON e compreensão de contexto histórico.

## Flags Aceitas

- `CTF{Seeing_The_Unseen}` — valor padrão.
- Instâncias personalizadas podem sobrescrever a flag via variável de ambiente `FLAG`.
