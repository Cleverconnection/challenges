FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc make && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY src /tmp/src
RUN mkdir -p /app/bin \
    && gcc /tmp/src/rt_core.c -o /app/bin/rt_core -lpthread \
    && rm -rf /tmp/src

COPY app /app
COPY config /app/config

CMD ["/app/start.sh"]
