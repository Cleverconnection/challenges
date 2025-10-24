# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS construtor
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /fonte
COPY src/printf_whisper.c ./
RUN gcc -Wall -Wextra -O0 -fno-stack-protector -no-pie -o printf_whisper printf_whisper.c

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m hopper
WORKDIR /home/hopper
COPY --from=construtor /fonte/printf_whisper ./printf_whisper
USER hopper
EXPOSE 1337
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/home/hopper/printf_whisper"]
