# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY src/hello_compiler.c ./
RUN gcc -Wall -Wextra -O2 -fno-plt -o hello_compiler hello_compiler.c

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m player
WORKDIR /opt/desafio
COPY --from=builder /build/hello_compiler ./hello_compiler
COPY README.md ./README.md
RUN chown player:player /opt/desafio/hello_compiler /opt/desafio/README.md
USER player
EXPOSE 3001
ENTRYPOINT ["socat", "-T", "60", "TCP-LISTEN:3001,reuseaddr,fork", "EXEC:/opt/desafio/hello_compiler,pty,raw,echo=0"]
