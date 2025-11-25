# Desafios Cleverconnection

A tabela abaixo lista todos os desafios, já com os diretórios renomeados sem os códigos numéricos. Cada linha informa a equipe-alvo (Red ou Blue Team), a dificuldade, a principal tecnologia/conceito explorado e a flag correspondente.

| Desafio | Equipe | Dificuldade | Tecnologia | Flag |
| --- | --- | --- | --- | --- |
| Loop Infinito Lunar | Blue Team | Fácil | loop infinito; liberar sentinela | `CTF{loop_infinito_corrigido}` |
| Corrida pelo Controle | Blue Team | Fácil | condição de corrida; habilitar trava | `CTF{condicao_de_corrida_domada}` |
| Agendador Caótico | Blue Team | Fácil | ajuste de prioridades do scheduler | `CTF{prioridades_em_orbita}` |
| Telemetria Sob Sobrecarga | Blue Team | Médio | logs em sobrecarga; alterar nível de log | `CTF{telemetria_em_modo_safe}` |
| Abort 1202 Revival | Blue Team | Difícil | alarme Abort 1202; reordenar tarefas | `CTF{abort_1202_superado}` |
| Guardiã das Árvores Digitais | Red Team | 180 | loop de rede e protocolo STP | `CTF{Arvores_Digitais_Seguras}` |
| Depuradora do Mark I | Blue Team | – | depuração de computador antigo | `CTF{Flowmatic_Debug_Master}` |
| Atlas de Visão | Blue Team | – | análise de rótulos de imagem | `CTF{Seeing_The_Unseen}` |
| Supervisora do Apollo | Blue Team | – | gerenciamento de alarmes críticos | `CTF{Software_On_The_Moon}` |
| Trinity — A Hacker que Libertou Consciências | Red Team | 100 | OSINT em banco de dados fictício | `CTF{Banco_de_Dados_da_Receita}` |
| Pioneiro do Futuro 1 | Blue Team | – | – | `–` |
| Desafio Provisório 1 | Blue Team | – | – | `–` |
| Weaving the Tree | Blue Team | 120 | – | `FLAG{root_32768_001122334466}` |
| Pioneiro do Futuro 2 | Blue Team | – | – | `–` |
| Desafio Provisório 2 | Blue Team | – | – | `–` |
| Root Bridge Live | Red Team | 150 | – | `CECYBER{root_change_detected}` |
| Pioneiro do Futuro 3 | Blue Team | – | – | `–` |
| Desafio Provisório 3 | Blue Team | – | – | `–` |
| STP Loop Recovery | Red Team | 150 | – | `CECYBER{loop_blocked_successfully}` |
| Pioneiro do Futuro 4 | Blue Team | – | – | `–` |
| Desafio Provisório 4 | Blue Team | – | – | `–` |
| Tree Guard | Blue Team | 150 | – | `CECYBER{falsa_root_00:11:22:33:44:99}` |
| Galeria de Prompts da Visionária | Red Team | 140 | – | `CECYBER{prompt_guard_breached}` |
| Atlas Visionário | Red Team | 200 | – | `CECYBER{analysis_mode_victory}` |
| Manual Público | Red Team | Fácil | Swagger expõe tokens e rotas internas | `CTF{swagger_spill}` |
| Cabeçalhos Reveladores | Red Team | Fácil | cabeçalhos vazam caminhos internos | `CTF{headers_tell_secrets}` |
| Desafio Futuro | Blue Team | – | – | `–` |
| Desafio Provisório | Blue Team | – | desafio não implementado | `–` |
| Link Compartilhado | Red Team | Fácil | – | `CTF{creds_in_query}` |
| Registros Não Confiáveis | Red Team | Fácil | injeção em logs | `CTF{logs_are_trust_issue}` |
| Transação Repetida | Red Team | Fácil | replay de timestamp | `CTF{timestamp_replay_attack}` |
| Token Frágil | Red Team | Fácil | criptografia sem IV | `CTF{weak_crypto_modes}` |
| Backup Público | Red Team | Fácil | backup público exposto | `CTF{public_backup_flag}` |
| Redefinição Generosa | Red Team | Fácil | enumeração de usuário via reset | `CTF{reset_enum_abuse}` |
| Transporte Opcional | Red Team | Fácil | sem redirecionamento HTTPS | `CTF{tls_redirect_missing}` |
| Download Genérico | Red Team | Fácil | path traversal em download | `CTF{file_download_traversal}` |
| Sessão Reutilizável | Red Team | Fácil | credenciais padrão fracas | `CTF{weak_passwords_ruin_security}` |
| Validador Infinito | Red Team | Fácil | brute force sem rate limit | `CTF{rate_limit_none}` |
| Chave Persistente | Red Team | Fácil | JWT sem expiração; alterar role | `CTF{jwt_without_expiration}` |
| Consulta por Identificador | Red Team | Fácil | IDOR via parâmetro id | `CTF{idor_bank_accounts}` |
| Requisição Transparente | Red Team | Fácil | proxy aberto / SSRF | `CTF{ssrf_proxy_to_flag}` |
| Leitor Amplo | Red Team | Fácil | directory traversal para ler arquivo | `CTF{path_traversal_master}` |
| Relatório Aberto | Red Team | Fácil | SQL Injection | `CTF{sqli_in_the_branch}` |
| Importação XML | Red Team | Fácil | XXE | `CTF{xxe_into_core}` |
| Envio Público | Red Team | Fácil | uploads previsíveis; enumerar | `CTF{predictable_upload_leak}` |
| Compartilhamento Cruzado | Red Team | Fácil | – | `CTF{cors_wildcard_token}` |
| Hello, Compiler | Blue Team | Fácil | ler .rodata de binário C | `CTF{grace_xor_matematica}` |
| Legacy Logger | Blue Team | Fácil | decodificar logs ROT13 | `CTF{grace_rot_traducao}` |
| Symbolic Pointer | Blue Team | Fácil | usar tabela de símbolos | `CTF{grace_symbol_legivel}` |
| Printf Whisper | Red Team | Médio | explorar vulnerabilidade de format string | `CTF{grace_printf_confiança}` |
| Compiler's Shadow | Red Team | Difícil | antidebugging e máquina de estados | `CTF{grace_shadow_otimizacao}` |
| Quem está na imagem? | Blue Team | – | enviar cor correta para API de cores | `CTF{fei_fei_memoria_azul}` |
| Correspondência pHash | Blue Team | Médio | comparar perceptual hash (pHash) | `CTF{fei_fei_phash_match}` |
| Viés de Rotulagem | Blue Team | Médio | corrigir viés nos rótulos | `CTF{fei_fei_bias_ajustado}` |
| Prompt Injection Vision | Red Team | Médio | injetar prompt [[INTERN]] | `CTF{fei_fei_prompt_fluxo}` |
| Trustworthy Model Escape | Red Team | Difícil | injetar mensagem LIBERAR_FLAG no pipeline | `CTF{fei_fei_pipeline_escape}` |
| MFA sem Ordem | Red Team | Médio | bypass de autenticação multi-fator | `CTF{auth_logic_mfa_bypass}` |
| Token Confuso | Red Team | Médio | confusão de kid e alg=none no JWT | `CTF{jwt_kid_none_alg}` |
| Proxy Cego | Red Team | Médio | SSRF para serviço interno via proxy | `CTF{ssrf_internal_service}` |
| Corrida de Transferências | Red Team | Médio | race condition em transferências | `CTF{race_condition_transfer}` |
| Pagamentos Replay | Red Team | Médio | replay de pagamento | `CTF{payment_replay_bonus}` |
| XML Explosivo | Red Team | Médio | XXE e DoS em XML | `CTF{xml_xxe_resource_exhaust}` |
| Job Java Inseguro | Red Team | Médio | desserialização insegura em Java | `CTF{java_insecure_deserialize}` |
| Artifact Exposure | Red Team | Médio | exposição de tokens de pipeline | `CTF{supply_chain_artifact}` |
| Patch Indireto | Red Team | Médio | campo role mal validado | `CTF{api_privilege_escalation}` |
| Proxy S3 Interno | Red Team | Médio | SSRF para bucket S3 interno | `CTF{ssrf_s3_traversal}` |
| Config Leak | Red Team | Médio | servidor de config vaza segredos | `CTF{config_endpoint_leak}` |
| OTP Previsível | Red Team | Médio | OTP previsível | `CTF{predictable_otp_bypass}` |
| CSRF API | Red Team | Médio | CSRF via CORS permissivo e cookie | `CTF{csrf_cookie_api}` |
| Fusão Curiosa | Red Team | Médio | fusão de contas vaza dados | `CTF{account_merge_disclosure}` |
| Metadata SSRF | Red Team | Médio | SSRF para serviço de metadados | `CTF{metadata_ssrf_flag}` |
| Saldo Negativo Corrida | Red Team | Médio | race condition no saldo | `CTF{race_negative_balance}` |
| Timing Attack | Red Team | Médio | ataque de temporização | `CTF{timing_leak_username}` |
| Object Storage Exposto | Red Team | Médio | path traversal em serviço de arquivos | `CTF{object_storage_flag}` |
| Authorization Split | Red Team | Médio | separação de header Authorization | `CTF{auth_header_split}` |
| Forensics Tamper | Red Team | Médio | manipulação de logs e exportação | `CTF{log_tamper_flag}` |
| Glitch na Simulação | Red Team | Fácil | XSS para roubar cookie | `CTF{Trinity_Glitch_Vigilia}` |
| Pílula Vermelha | Red Team | Fácil | listagem de diretórios | `CTF{Trinity_Pilula_Listagem}` |
| Eco do Oráculo | Red Team | Fácil | upload inseguro e logs | `CTF{Trinity_Log_Do_Oraculo}` |
| Porta 22 de Zion | Red Team | Difícil | reconstruir credenciais SSH | `CTF{Trinity_Zion_SSH}` |
| Quebrando a Arquitetura | Red Team | Difícil | LFI + log poisoning + HMAC | `CTF{Trinity_Arquitetura_Liberada}` |
