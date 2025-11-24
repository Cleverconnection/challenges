# Classificação Red Team / Blue Team

A tabela abaixo apresenta os desafios do repositório **Cleverconnection/challenges**, classificando‑os como **Red Team** (ofensivo) ou **Blue Team** (defensivo/análise) e oferecendo um motivo breve.  As descrições resumidas vêm do README do projeto, que lista o conceito explorado em cada desafio【648393380382375†L425-L438】【648393380382375†L459-L478】. Os julgamentos Red/Blue baseiam‑se no tipo de atividade: exploração de vulnerabilidade ou ataque (Red) versus correção, análise ou mitigação (Blue).  Para desafios sem descrição, a classificação é estimada a partir do tema sugerido no identificador.

| Desafio | Classificação | Motivo (resumido) |
| --- | --- | --- |
| **A01_loop_infinito_lunar** | Blue Team | Trata de loop infinito em sistema embarcado; o objetivo é estabilizar a navegação e liberar sentinela【197662196715483†L0-L18】. |
| **A02_corrida_controle** | Blue Team | Corrida de controle em subsistemas; corrigir condição de corrida e habilitar trava de coordenação【197662196715483†L0-L18】. |
| **A03_agendador_caotico** | Blue Team | Ajustar prioridades do scheduler de um sistema embarcado (engenharia de confiabilidade). |
| **A04_telemetria_sob_sobrecarga** | Blue Team | Desafio de logs sob sobrecarga; alterar nível de log para manter estabilidade【648393380382375†L436-L437】. |
| **A05_abort_1202_revival** | Blue Team | Reordenar tarefas e lidar com alarme Abort 1202 (falha de timing); foco em correção【648393380382375†L438-L439】. |
| **B01_radia_perlman** | Red Team | Loop de rede e protocolo STP; envolve criação/exploração de loop de rede【648393380382375†L440-L448】. |
| **B02_grace_hopper** | Blue Team | Depuração de computador antigo; sugere análise/debug em vez de ataque. |
| **B03_fei_fei_li** | Blue Team | Análise de rótulos de imagem; alinhado à correção de viés ou rotulagem (não ofensivo). |
| **B04_margaret_hamilton** | Blue Team | Gerenciamento de alarmes críticos; foco em robustez de sistemas. |
| **B05_trinity_matrix** | Red Team | OSINT em banco de dados fictício; coleta e exploração de dados públicos. |
| **B06_pioneer_future** | Desconhecido | Falta descrição; não classificado. |
| **B06_provisional** | Desconhecido | Placeholder sem desafio implementado. |
| **B06_radia_perlman** | Blue Team | Forensics digital (classificado como forense na tabela【648393380382375†L444-L448】). |
| **B07_pioneer_future** | Desconhecido | Sem descrição. |
| **B07_provisional** | Desconhecido | Sem descrição. |
| **B07_radia_perlman** | Red Team | Desafio de rede (network) com ênfase em exploração【648393380382375†L449-L453】. |
| **B08_pioneer_future** | Desconhecido | Sem descrição. |
| **B08_provisional** | Desconhecido | Sem descrição. |
| **B08_radia_perlman** | Red Team | Desafio de rede (network), possivelmente exploração de STP/loop【648393380382375†L449-L453】. |
| **B09_pioneer_future** | Desconhecido | Sem descrição. |
| **B09_provisional** | Desconhecido | Sem descrição. |
| **B09_radia_perlman** | Blue Team | Descrito como forense【648393380382375†L454-L456】; análise de vestígios digitais. |
| **B10_fei_fei_li** | Blue Team | Desafio Web (140 pontos), provavelmente sobre rotulagem ou classificação (defensivo). |
| **B11_fei_fei_li** | Blue Team | Desafio Web (200 pontos), alinhado à análise defensiva. |
| **E10_exposed_swagger** | Red Team | Explora um Swagger que expõe tokens/rotas internas【648393380382375†L459-L462】. |
| **E11_info_headers** | Red Team | Vazamento de caminhos internos via cabeçalhos HTTP; exploração de informação【648393380382375†L459-L462】. |
| **E12_future_challenge** | Desconhecido | Não implementado. |
| **E12_provisional** | Desconhecido | Placeholder. |
| **E12_query_creds** | Red Team | Desafio Web fácil, envolvendo consulta de credenciais. |
| **E13_log_injection** | Red Team | Injeção em logs (log poisoning)【648393380382375†L464-L478】; ofensivo. |
| **E14_timestamp_replay** | Red Team | Explora replay de timestamp; típico ataque de repetição. |
| **E15_weak_crypto** | Red Team | Criptografia sem IV; exploração de fraqueza criptográfica. |
| **E16_public_backup** | Red Team | Backup público exposto; exploração de dados sensíveis【648393380382375†L466-L469】. |
| **E17_password_reset_enum** | Red Team | Enumeração de usuários via reset de senha【648393380382375†L468-L470】. |
| **E18_missing_tls_redirect** | Red Team | Falta de redirecionamento HTTPS; permite captura/brute force. |
| **E19_file_download_path** | Red Team | Path traversal em download de arquivo【648393380382375†L470-L476】. |
| **E1_auth_weak_pwd** | Red Team | Uso de credenciais padrão fracas【648393380382375†L470-L472】. |
| **E20_rate_limit_none** | Red Team | Brute force sem rate limit【648393380382375†L468-L472】. |
| **E2_jwt_noexp** | Red Team | JWT sem expiração e alteração de role【648393380382375†L472-L474】. |
| **E3_idor_account** | Red Team | IDOR via parâmetro `id`【648393380382375†L474-L475】. |
| **E4_open_redirect** | Red Team | Proxy aberto/SSRF【648393380382375†L475-L476】. |
| **E5_file_read** | Red Team | Directory traversal para ler arquivos【648393380382375†L476-L476】. |
| **E6_sql_injection_basic** | Red Team | SQL injection básico【648393380382375†L477-L478】. |
| **E7_xxe_simple** | Red Team | XXE básico【648393380382375†L478-L478】. |
| **E8_upload_exec_hint** | Red Team | Uploads previsíveis e enumeráveis【648393380382375†L478-L479】. |
| **E9_cors_wildcard** | Red Team | CORS permissivo; exploração de origem cruzada【648393380382375†L478-L480】. |
| **G01_hello_compiler** | Red Team | Leitura da seção `.rodata` de binário C; típica engenharia reversa/exploits【648393380382375†L481-L482】. |
| **G02_legacy_logger** | Blue Team | Decodificar logs em ROT13【648393380382375†L482-L483】; atividade de análise. |
| **G03_symbolic_pointer** | Red Team | Uso de tabela de símbolos para explorar ponteiros e memória【648393380382375†L482-L484】. |
| **G04_printf_whisper** | Red Team | Exploração de vulnerabilidade de format string【648393380382375†L484-L485】. |
| **G05_compilers_shadow** | Red Team | Antidebugging e máquina de estados; envolve evadir defesas【648393380382375†L485-L486】. |
| **G06_who_is_in_the_image** | Blue Team | Enviar cor correta para API de cores; exercício de visão computacional não ofensivo. |
| **G07_phash_match** | Blue Team | Comparar perceptual hash (pHash); tarefa analítica【648393380382375†L487-L489】. |
| **G08_labeling_bias** | Blue Team | Corrigir viés nos rótulos de treinamento【648393380382375†L488-L489】. |
| **G09_prompt_inject_vision** | Red Team | Injeção de prompt em modelo de visão computacional【648393380382375†L489-L490】. |
| **G10_trustworthy_model_escape** | Red Team | Injetar mensagem para liberar flag em pipeline de visão【648393380382375†L490-L492】. |
| **M01_auth_bypass_logic** | Red Team | Bypass de autenticação multi‑fator【648393380382375†L493-L498】. |
| **M02_jwt_kid_attack** | Red Team | Confusão do campo `kid` e uso de `alg=none` em JWT【648393380382375†L493-L498】. |
| **M03_ssrf_internal_svc** | Red Team | SSRF para serviço interno via proxy【648393380382375†L495-L498】. |
| **M04_concurrent_transfer_race** | Red Team | Race condition em transferências【648393380382375†L496-L497】. |
| **M05_payment_replay** | Red Team | Replay de pagamento【648393380382375†L496-L497】. |
| **M06_xml_dos_xxe_combo** | Red Team | XXE e DoS em XML【648393380382375†L498-L499】. |
| **M07_insecure_deserialize** | Red Team | Desserialização insegura em Java【648393380382375†L499-L499】. |
| **M08_supply_chain_devops** | Red Team | Exposição de tokens de pipeline【648393380382375†L499-L501】. |
| **M09_privilege_escalation_api** | Red Team | Escalada de privilégio via campo `role` mal validado【648393380382375†L499-L501】. |
| **M10_ssrf_s3_misuse** | Red Team | SSRF para bucket S3 interno【648393380382375†L502-L503】. |
| **M11_confd_leak** | Red Team | Servidor de configuração vaza segredos【648393380382375†L503-L504】. |
| **M12_otp_bypass** | Red Team | OTP previsível (bypass)【648393380382375†L504-L505】. |
| **M13_csrf_api** | Red Team | CSRF via CORS permissivo e cookie【648393380382375†L505-L506】. |
| **M14_account_merge_bug** | Red Team | Falha na fusão de contas vazando dados【648393380382375†L506-L507】. |
| **M15_ssrf_internal_metadata** | Red Team | SSRF para serviço de metadados【648393380382375†L507-L508】. |
| **M16_race_balance_check** | Red Team | Condição de corrida no saldo de conta【648393380382375†L508-L509】. |
| **M17_timing_attack** | Red Team | Ataque de temporização【648393380382375†L509-L509】. |
| **M18_insecure_file_serve** | Red Team | Path traversal em serviço de arquivos【648393380382375†L510-L510】. |
| **M19_authorization_header_splitting** | Red Team | Separação do header `Authorization`【648393380382375†L510-L511】. |
| **M20_log_forensics_tamper** | Red Team | Manipulação/remoção de logs; ofensivo pois visa evadir detecção【648393380382375†L512-L513】. |
| **T1_glitch_na_simulacao** | Red Team | XSS para roubar cookies【648393380382375†L514-L515】. |
| **T2_pilula_vermelha** | Red Team | Listagem de diretórios (exposição de arquivos)【648393380382375†L515-L515】. |
| **T3_eco_do_oraculo** | Red Team | Upload inseguro e exploração de logs【648393380382375†L516-L516】. |
| **T4_porta_22_de_zion** | Red Team | Reconstruir credenciais SSH; ataque de força bruta/inferência. |
| **T5_quebrando_a_arquitetura** | Red Team | LFI + log poisoning + HMAC; exploração complexa【648393380382375†L517-L518】. |

**Observação:** Desafios marcados como “Desconhecido” não possuem descrição suficiente no README para uma classificação segura.  Se essa informação for disponibilizada nos arquivos `challenge.yml` ou write‑ups, a classificação pode ser revisada.
