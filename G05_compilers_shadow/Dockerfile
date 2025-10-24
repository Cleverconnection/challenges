# syntax=docker/dockerfile:1

FROM debian:bookworm-slim AS construtor
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /fonte
COPY src/compilers_shadow.c ./
RUN gcc -O2 -Wall -Wextra -fno-stack-protector -no-pie -o compilers_shadow compilers_shadow.c

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m hopper
WORKDIR /home/hopper
COPY --from=construtor /fonte/compilers_shadow ./compilers_shadow
USER hopper
EXPOSE 2222
CMD ["socat", "TCP-LISTEN:2222,reuseaddr,fork", "EXEC:/home/hopper/compilers_shadow"]
