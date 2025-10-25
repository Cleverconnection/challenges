FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    SSH_PORT=2223 \
    CHALLENGE_CMD="python /opt/desafio/app/scheduler.py"

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash player \
    && echo 'player:player' | chpasswd
RUN mkdir -p /var/run/sshd /var/log/navegadora \
    && chown player:player /var/log/navegadora

WORKDIR /opt/desafio
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY config ./config
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh \
    && chown -R player:player /opt/desafio

EXPOSE 2223
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
