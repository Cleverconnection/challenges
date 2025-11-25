# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY src/compilers_shadow.c ./
RUN gcc -O2 -Wall -Wextra -fno-stack-protector -no-pie -o compilers_shadow compilers_shadow.c

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m player
WORKDIR /opt/desafio
COPY --from=builder /build/compilers_shadow ./compilers_shadow
COPY README.md ./README.md
RUN chown player:player /opt/desafio/compilers_shadow /opt/desafio/README.md
USER player
EXPOSE 3005
ENTRYPOINT ["socat", "-T", "60", "TCP-LISTEN:3005,reuseaddr,fork", "EXEC:/opt/desafio/compilers_shadow,pty,raw,echo=0"]
