# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY src/symbolic_pointer.c ./
RUN gcc -Wall -g -O1 -o symbolic_pointer symbolic_pointer.c

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m player
WORKDIR /opt/desafio
COPY --from=builder /build/symbolic_pointer ./symbolic_pointer
COPY README.md ./README.md
RUN chown player:player /opt/desafio/symbolic_pointer /opt/desafio/README.md
USER player
EXPOSE 3003
ENTRYPOINT ["socat", "-T", "60", "TCP-LISTEN:3003,reuseaddr,fork", "EXEC:/opt/desafio/symbolic_pointer,pty,raw,echo=0"]
