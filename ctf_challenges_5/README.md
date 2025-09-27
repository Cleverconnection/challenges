# Itaú CTF – Pacote de Desafios (E1–E20)

Este diretório reúne vinte desafios independentes em Flask pensados para a edição 2025 do CTF Itaú. Cada serviço possui front-end padronizado com a identidade visual solicitada e um Dockerfile dedicado para facilitar o build e a publicação em ambientes CTFd, Proxmox ou infraestrutura similar.

## Visão geral dos desafios

| Desafio | Tema | Enredo | Flag padrão |
|---------|------|--------|-------------|
| `E1_auth_weak_pwd` | Autenticação | Portal legado usa senhas triviais para gerar tokens internos. | `ITAU2025{weak_passwords_ruin_security}` |
| `E2_jwt_noexp` | API JWT | Token sem expiração permite manipular o payload para escalar privilégios. | `ITAU2025{jwt_without_expiration}` |
| `E3_idor_account` | IDOR | Consulta de contas não verifica o proprietário e expõe dados executivos. | `ITAU2025{idor_bank_accounts}` |
| `E4_open_redirect` | SSRF | Proxy de integrações faz fetch de qualquer URL informada pelo operador. | `ITAU2025{ssrf_proxy_to_flag}` |
| `E5_file_read` | Path traversal | Leitor corporativo acessa caminhos arbitrários dentro do container. | `ITAU2025{path_traversal_master}` |
| `E6_sql_injection_basic` | SQL Injection | Relatório comercial monta consultas com concatenação simples permitindo UNION. | `ITAU2025{sqli_in_the_branch}` |
| `E7_xxe_simple` | XXE | Importador XML aceita entidades externas e revela códigos internos. | `ITAU2025{xxe_into_core}` |
| `E8_upload_exec_hint` | Upload inseguro | Central de uploads publica arquivos com nomes previsíveis ao lado de notas sigilosas. | `ITAU2025{predictable_upload_leak}` |
| `E9_cors_wildcard` | CORS | API responde com `Access-Control-Allow-Origin: *`, expondo o token de sessão. | `ITAU2025{cors_wildcard_token}` |
| `E10_exposed_swagger` | Swagger público | Documentação interna vazou com exemplos contendo chaves reais. | `ITAU2025{swagger_spill}` |
| `E11_info_headers` | Headers verbosos | Healthcheck entrega cabeçalhos com caminhos e dicas de arquivos sensíveis. | `ITAU2025{headers_tell_secrets}` |
| `E12_query_creds` | Credenciais na URL | Link de backup inclui token em query string compartilhado por e-mail. | `ITAU2025{creds_in_query}` |
| `E13_log_injection` | Log injection | Painel de incidentes grava input bruto permitindo forjar entradas válidas. | `ITAU2025{logs_are_trust_issue}` |
| `E14_timestamp_replay` | Replay de transações | Motor antifraude aceita o mesmo timestamp diversas vezes e acumula créditos. | `ITAU2025{timestamp_replay_attack}` |
| `E15_weak_crypto` | Criptografia fraca | Tokens usam AES-ECB com chave derivada em MD5, permitindo corte e montagem. | `ITAU2025{weak_crypto_modes}` |
| `E16_public_backup` | Backup público | Arquivo `backup.zip` fica acessível na raiz com flag embutida. | `ITAU2025{public_backup_flag}` |
| `E17_password_reset_enum` | Enumeração | Portal de reset aceita qualquer ID numérico e retorna link privilegiado. | `ITAU2025{reset_enum_abuse}` |
| `E18_missing_tls_redirect` | TLS opcional | Serviço expõe cookies de sessão mesmo quando acessado via HTTP. | `ITAU2025{tls_redirect_missing}` |
| `E19_file_download_path` | Download inseguro | Endpoint de download concatena caminhos permitindo fuga do diretório. | `ITAU2025{file_download_traversal}` |
| `E20_rate_limit_none` | Brute force | Validador de OTP não impõe rate limit, permitindo força bruta ao token. | `ITAU2025{rate_limit_bypass}` |

## Estrutura

```
ctf_challenges_5/
  E*/
    app.py         # Aplicação Flask vulnerável
    templates/     # Front-end com identidade visual unificada
    Dockerfile     # Receita da imagem do container
```

Todos os serviços escrevem a flag padrão em `/flag` durante a inicialização, permitindo integração com checagens automatizadas. As flags podem ser sobrescritas via variável de ambiente `FLAG` no `docker run` se necessário.

## Como construir

Cada desafio pode ser construído individualmente:

```bash
cd ctf_challenges_5/E6_sql_injection_basic
sudo docker build -t ctf/e6_sql_injection_basic:latest .
```

Altere o diretório/tag conforme o desafio desejado (`E1` até `E20`).

## Como executar localmente

```bash
sudo docker run -it --rm \
  -p 15006:8080 \
  ctf/e6_sql_injection_basic:latest
```

Defina `FLAG="ITAU2025{custom}"` durante o `docker run` se quiser personalizar uma instância específica.

## Observações

- Nenhum desafio implementa controles de segurança reais; use apenas em ambientes isolados.
- Os front-ends seguem o layout escuro solicitado e oferecem dicas narrativas para orientar os participantes.
- Recursos auxiliares (arquivos, bancos, logs) são criados automaticamente dentro do container na primeira execução.

Bom CTF! 🏦
