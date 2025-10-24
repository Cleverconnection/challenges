# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS construtor
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /fonte
COPY src/hello_compiler.c ./
RUN gcc -Wall -Wextra -O2 -fno-plt -o hello_compiler hello_compiler.c

FROM debian:bookworm-slim
RUN useradd -m hopper
WORKDIR /opt/desafio
COPY --from=construtor /fonte/hello_compiler ./hello_compiler
COPY README.md ./README.md
USER hopper
ENTRYPOINT ["./hello_compiler"]
