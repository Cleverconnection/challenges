# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY src/printf_whisper.c ./
RUN gcc -Wall -Wextra -O0 -fno-stack-protector -no-pie -o printf_whisper printf_whisper.c

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m player
WORKDIR /opt/desafio
COPY --from=builder /build/printf_whisper ./printf_whisper
COPY README.md ./README.md
RUN chown player:player /opt/desafio/printf_whisper /opt/desafio/README.md
USER player
EXPOSE 3004
ENTRYPOINT ["socat", "-T", "60", "TCP-LISTEN:3004,reuseaddr,fork", "EXEC:/opt/desafio/printf_whisper,pty,raw,echo=0"]
