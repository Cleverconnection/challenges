# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS construtor
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /fonte
COPY src/symbolic_pointer.c ./
RUN gcc -Wall -Wextra -O2 -o symbolic_pointer symbolic_pointer.c

FROM debian:bookworm-slim
RUN useradd -m hopper
WORKDIR /opt/desafio
COPY --from=construtor /fonte/symbolic_pointer ./symbolic_pointer
COPY README.md ./README.md
USER hopper
ENTRYPOINT ["./symbolic_pointer"]
