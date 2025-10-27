FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    SSH_PORT=2224 \
    CHALLENGE_CMD="sh /opt/desafio/app/start.sh"

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
COPY data ./data
COPY static ./static
COPY templates ./templates
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh /opt/desafio/app/start.sh \
    && chown -R player:player /opt/desafio
RUN ln -s /opt/desafio/app /app
   

EXPOSE 2224 5000
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
