# Itaú CTF – Pacote de Desafios (E1–E5)

Este diretório contém cinco desafios em formato de containers independentes para uso em um CTF baseado em CTFd, Proxmox ou infraestrutura similar. Cada desafio possui uma aplicação Flask com um front-end simples voltado para laboratório e o respectivo `Dockerfile` para geração da imagem.

## Visão geral dos desafios

| Desafio | Tema | Vetor explorado |
|---------|------|-----------------|
| `E1_auth_weak_pwd` | Portal de autenticação | Senhas fracas armazenadas em texto puro. |
| `E2_jwt_noexp` | API com JWT | Token sem expiração permitindo manipulação do payload. |
| `E3_idor_account` | Consulta de contas | Falta de controle de acesso nas rotas de conta (IDOR). |
| `E4_open_redirect` | Proxy SSRF | Proxy que busca URLs arbitrárias sem validação. |
| `E5_file_read` | File reader | Junção de caminhos vulnerável a path traversal. |

## Flags fixas

Cada serviço já inclui uma flag padrão pensada para o evento de 2025. Elas também são gravadas automaticamente em `/flag` durante o start do container.

| Desafio | Flag padrão |
|---------|-------------|
| `E1_auth_weak_pwd` | `ITAU2025{weak_passwords_ruin_security}` |
| `E2_jwt_noexp` | `ITAU2025{jwt_without_expiration}` |
| `E3_idor_account` | `ITAU2025{idor_bank_accounts}` |
| `E4_open_redirect` | `ITAU2025{ssrf_proxy_to_flag}` |
| `E5_file_read` | `ITAU2025{path_traversal_master}` |

## Estrutura

```
ctf_challenges_5/
  E*/
    app.py         # Aplicação Flask vulnerável
    templates/     # Front-end amigável para o desafio
    Dockerfile     # Receita da imagem do container
```

## Como construir

Cada desafio pode ser construído de forma independente:

```bash
cd ctf_challenges_5/E1_auth_weak_pwd
sudo docker build -t ctf/e1_auth_weak_pwd:latest .
```

Altere o diretório e a tag conforme o desafio desejado (`E2`, `E3`, etc.).

## Como executar localmente

```bash
sudo docker run -it --rm \
  -p 15001:8080 \
  ctf/e1_auth_weak_pwd:latest
```

Se desejar alterar a flag para uma instância específica, defina a variável de ambiente `FLAG` durante o `docker run`.

## Observações

- Os desafios não implementam mecanismos de proteção deliberadamente.
- O front-end facilita o onboarding de participantes e pode ser customizado com identidade visual.
- Certifique-se de isolar os containers em ambientes seguros e descartar após o evento.

Bom CTF! 🏦
