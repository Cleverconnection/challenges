FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    SSH_PORT=2221 \
    CHALLENGE_CMD="python /opt/desafio/app/loop.py"

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash player \
    && echo 'player:player' | chpasswd
RUN mkdir -p /var/run/sshd /var/log/navegadora \
    && chown player:player /var/log/navegadora

WORKDIR /opt/desafio
COPY app ./app
COPY config ./config
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh \
    && chown -R player:player /opt/desafio

EXPOSE 2221
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
