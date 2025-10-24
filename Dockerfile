# syntax=docker/dockerfile:1

FROM python:3.11-slim AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

# Build binaries for the G-series challenges
COPY G01_hello_compiler/src/hello_compiler.c G01_hello_compiler/src/hello_compiler.c
RUN mkdir -p bin \
    && gcc -Wall -Wextra -O2 -fno-plt -o bin/hello_compiler G01_hello_compiler/src/hello_compiler.c

COPY G03_symbolic_pointer/src/symbolic_pointer.c G03_symbolic_pointer/src/symbolic_pointer.c
RUN gcc -Wall -Wextra -O2 -o bin/symbolic_pointer G03_symbolic_pointer/src/symbolic_pointer.c

COPY G04_printf_whisper/src/printf_whisper.c G04_printf_whisper/src/printf_whisper.c
RUN gcc -Wall -Wextra -O0 -fno-stack-protector -no-pie -o bin/printf_whisper G04_printf_whisper/src/printf_whisper.c

COPY G05_compilers_shadow/src/compilers_shadow.c G05_compilers_shadow/src/compilers_shadow.c
RUN gcc -O2 -Wall -Wextra -fno-stack-protector -no-pie -o bin/compilers_shadow G05_compilers_shadow/src/compilers_shadow.c


FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/challenges

# Copy compiled binaries
COPY --from=builder /build/bin ./bin

# Copy source assets for each challenge
COPY G02_legacy_logger/app ./G02/app
COPY G02_legacy_logger/data ./G02/data
COPY G02_legacy_logger/requirements.txt ./G02/requirements.txt

COPY A01_loop_infinito_lunar/app ./A01/app
COPY A01_loop_infinito_lunar/config ./A01/config

COPY A02_corrida_controle/app ./A02/app
COPY A02_corrida_controle/config ./A02/config

COPY A03_agendador_caotico/app ./A03/app
COPY A03_agendador_caotico/config ./A03/config
COPY A03_agendador_caotico/requirements.txt ./A03/requirements.txt

COPY A04_telemetria_sob_sobrecarga/app ./A04/app
COPY A04_telemetria_sob_sobrecarga/config ./A04/config
COPY A04_telemetria_sob_sobrecarga/templates ./A04/templates
COPY A04_telemetria_sob_sobrecarga/static ./A04/static
COPY A04_telemetria_sob_sobrecarga/data ./A04/data
COPY A04_telemetria_sob_sobrecarga/requirements.txt ./A04/requirements.txt

# Install Python dependencies shared across the challenges
RUN pip install Flask==3.0.3 PyYAML==6.0.2

# Helper script to orchestrate the challenges
COPY scripts/start_challenge.sh /usr/local/bin/start_challenge.sh
RUN chmod +x /usr/local/bin/start_challenge.sh

EXPOSE 7001 7002 7003 7004 7005 7101 7102 7103 7104

ENTRYPOINT ["start_challenge.sh"]
