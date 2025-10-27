# Desafios Cleverconnection

A tabela abaixo resume todos os desafios disponíveis no repositório.

| ID                                 | Categoria           | Conceito explorado                        | Dificuldade | Flag |
| ---------------------------------- | ------------------- | ----------------------------------------- | ----------- | ---- |
| A01_loop_infinito_lunar            | Sistemas Embarcados | loop infinito; liberar sentinela          | **Fácil**   | –    |
| A02_corrida_controle               | Sistemas Embarcados | condição de corrida; habilitar trava      | **Fácil**   | –    |
| A03_agendador_caotico              | Sistemas Embarcados | ajuste de prioridades do scheduler        | **Fácil**   | –    |
| A04_telemetria_sob_sobrecarga      | Sistemas Embarcados | logs em sobrecarga; alterar nível de log  | **Médio**   | –    |
| A05_abort_1202_revival             | Sistemas Embarcados | alarme Abort 1202; reordenar tarefas      | **Difícil** | –    |
| B01_radia_perlman                  | Web                 | loop de rede e protocolo STP              | 180         | –    |
| B02_grace_hopper                   | –                   | depuração de computador antigo            | –           | –    |
| B03_fei_fei_li                     | –                   | análise de rótulos de imagem              | –           | –    |
| B04_margaret_hamilton              | –                   | gerenciamento de alarmes críticos         | –           | –    |
| B05_trinity_matrix                 | Cultura Pop / OSINT | OSINT em banco de dados fictício          | 100         | –    |
| B06_pioneer_future                 | –                   |                                           | –           | –    |
| B06_provisional                    | –                   |                                           | –           | –    |
| B06_radia_perlman                  | Forensics           |                                           | 120         | –    |
| B07_pioneer_future                 | –                   |                                           | –           | –    |
| B07_provisional                    | –                   |                                           | –           | –    |
| B07_radia_perlman                  | Network             |                                           | 150         | –    |
| B08_pioneer_future                 | –                   |                                           | –           | –    |
| B08_provisional                    | –                   |                                           | –           | –    |
| B08_radia_perlman                  | Network             |                                           | 150         | –    |
| B09_pioneer_future                 | –                   |                                           | –           | –    |
| B09_provisional                    | –                   |                                           | –           | –    |
| B09_radia_perlman                  | Forensics           |                                           | 150         | –    |
| B10_fei_fei_li                     | Web                 |                                           | 140         | –    |
| B11_fei_fei_li                     | Web                 |                                           | 200         | –    |
| E10_exposed_swagger                | Web                 | Swagger expõe tokens e rotas internas     | **Fácil**   | –    |
| E11_info_headers                   | Web                 | cabeçalhos vazam caminhos internos        | **Fácil**   | –    |
| E12_future_challenge               | –                   |                                           | –           | –    |
| E12_provisional                    | –                   | desafio não implementado                  | –           | –    |
| E12_query_creds                    | Web                 |                                           | **Fácil**   | –    |
| E13_log_injection                  | Web                 | injeção em logs                           | **Fácil**   | –    |
| E14_timestamp_replay               | Web                 | replay de timestamp                       | **Fácil**   | –    |
| E15_weak_crypto                    | Web                 | criptografia sem IV                       | **Fácil**   | –    |
| E16_public_backup                  | Web                 | backup público exposto                    | **Fácil**   | –    |
| E17_password_reset_enum            | Web                 | enumeração de usuário via reset           | **Fácil**   | –    |
| E18_missing_tls_redirect           | Web                 | sem redirecionamento HTTPS                | **Fácil**   | –    |
| E19_file_download_path             | Web                 | path traversal em download                | **Fácil**   | –    |
| E1_auth_weak_pwd                   | Web                 | credenciais padrão fracas                 | **Fácil**   | –    |
| E20_rate_limit_none                | Web                 | brute force sem rate limit                | **Fácil**   | –    |
| E2_jwt_noexp                       | Web                 | JWT sem expiração; alterar role           | **Fácil**   | –    |
| E3_idor_account                    | Web                 | IDOR via parâmetro id                     | **Fácil**   | –    |
| E4_open_redirect                   | Web                 | proxy aberto / SSRF                       | **Fácil**   | –    |
| E5_file_read                       | Web                 | directory traversal para ler arquivo      | **Fácil**   | –    |
| E6_sql_injection_basic             | Web                 | SQL Injection                             | **Fácil**   | –    |
| E7_xxe_simple                      | Web                 | XXE                                       | **Fácil**   | –    |
| E8_upload_exec_hint                | Web                 | uploads previsíveis; enumerar             | **Fácil**   | –    |
| E9_cors_wildcard                   | Web                 |                                           | **Fácil**   | –    |
| G01_hello_compiler                 | Programação         | ler .rodata de binário C                  | **Fácil**   | –    |
| G02_legacy_logger                  | Programação         | decodificar logs ROT13                    | **Fácil**   | –    |
| G03_symbolic_pointer               | Programação         | usar tabela de símbolos                   | **Fácil**   | –    |
| G04_printf_whisper                 | Programação         | explorar vulnerabilidade de format string | **Médio**   | –    |
| G05_compilers_shadow               | Programação         | antidebugging e máquina de estados        | **Difícil** | –    |
| G06_who_is_in_the_image            | –                   | enviar cor correta para API de cores      | –           | –    |
| G07_phash_match                    | Visão Computacional | comparar perceptual hash (pHash)          | **Médio**   | –    |
| G08_labeling_bias                  | Visão Computacional | corrigir viés nos rótulos                 | **Médio**   | –    |
| G09_prompt_inject_vision           | Visão Computacional | injetar prompt [[INTERN]]                 | **Médio**   | –    |
| G10_trustworthy_model_escape       | Visão Computacional | injetar mensagem LIBERAR_FLAG no pipeline | **Difícil** | –    |
| M01_auth_bypass_logic              | Web                 | bypass de autenticação multi-fator        | **Médio**   | –    |
| M02_jwt_kid_attack                 | Web                 | confusão de kid e alg=none no JWT         | **Médio**   | –    |
| M03_ssrf_internal_svc              | Web                 | SSRF para serviço interno via proxy       | **Médio**   | –    |
| M04_concurrent_transfer_race       | Web                 | race condition em transferências          | **Médio**   | –    |
| M05_payment_replay                 | Web                 | replay de pagamento                       | **Médio**   | –    |
| M06_xml_dos_xxe_combo              | Web                 | XXE e DoS em XML                          | **Médio**   | –    |
| M07_insecure_deserialize           | Web                 | desserialização insegura em Java          | **Médio**   | –    |
| M08_supply_chain_devops            | Web                 | exposição de tokens de pipeline           | **Médio**   | –    |
| M09_privilege_escalation_api       | Web                 | campo role mal validado                   | **Médio**   | –    |
| M10_ssrf_s3_misuse                 | Web                 | SSRF para bucket S3 interno               | **Médio**   | –    |
| M11_confd_leak                     | Web                 | servidor de config vaza segredos          | **Médio**   | –    |
| M12_otp_bypass                     | Web                 | OTP previsível                            | **Médio**   | –    |
| M13_csrf_api                       | Web                 | CSRF via CORS permissivo e cookie         | **Médio**   | –    |
| M14_account_merge_bug              | Web                 | fusão de contas vaza dados                | **Médio**   | –    |
| M15_ssrf_internal_metadata         | Web                 | SSRF para serviço de metadados            | **Médio**   | –    |
| M16_race_balance_check             | Web                 | race condition no saldo                   | **Médio**   | –    |
| M17_timing_attack                  | Web                 | ataque de temporização                    | **Médio**   | –    |
| M18_insecure_file_serve            | Web                 | path traversal em serviço de arquivos     | **Médio**   | –    |
| M19_authorization_header_splitting | Web                 | separação de header Authorization         | **Médio**   | –    |
| M20_log_forensics_tamper           | Web                 | manipulação de logs e exportação          | **Médio**   | –    |
| T1_glitch_na_simulacao             | Web                 | XSS para roubar cookie                    | **Fácil**   | –    |
| T2_pilula_vermelha                 | Web                 | listagem de diretórios                    | **Fácil**   | –    |
| T3_eco_do_oraculo                  | Web                 | upload inseguro e logs                    | **Fácil**   | –    |
| T4_porta_22_de_zion                | Web                 | reconstruir credenciais SSH               | **Difícil** | –    |
| T5_quebrando_a_arquitetura         | Web                 | LFI + log poisoning + HMAC                | **Difícil** | –    |
