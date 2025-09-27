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
  -e FLAG="CTF{FLAG_REAL}" \
  -p 15001:8080 \
  ctf/e1_auth_weak_pwd:latest
```

A flag também é escrita em `/flag` dentro do container, facilitando integrações com scripts de verificação.

## Observações

- Os desafios não implementam mecanismos de proteção deliberadamente.
- O front-end facilita o onboarding de participantes e pode ser customizado com identidade visual.
- Certifique-se de isolar os containers em ambientes seguros e descartar após o evento.

Bom CTF! 🏦
