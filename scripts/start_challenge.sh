#!/bin/sh
set -e

if [ -z "$CHALLENGE" ]; then
    echo "Erro: defina a variável de ambiente CHALLENGE com um dos valores A01, A02, A03, A04, G01, G02, G03, G04 ou G05." >&2
    exit 1
fi

challenge="$(printf '%s' "$CHALLENGE" | tr '[:lower:]' '[:upper:]')"

prepare_python_challenge() {
    desafio="$1"
    base="/opt/challenges/${desafio}"

    rm -rf /app /data
    if [ -d "${base}/app" ]; then
        mkdir -p /app
        cp -a "${base}/app/." /app/
    fi
    if [ -d "${base}/config" ]; then
        mkdir -p /app/config
        cp -a "${base}/config/." /app/config/
    fi
    if [ -d "${base}/templates" ]; then
        mkdir -p /app/templates
        cp -a "${base}/templates/." /app/templates/
    fi
    if [ -d "${base}/static" ]; then
        mkdir -p /app/static
        cp -a "${base}/static/." /app/static/
    fi
    if [ -d "${base}/data" ]; then
        mkdir -p /data
        cp -a "${base}/data/." /data/
    fi
}

run_with_socat() {
    porta_default="$1"
    comando="$2"

    porta="${PORT:-${porta_default}}"
    echo "Iniciando serviço na porta ${porta}."
    exec socat "TCP-LISTEN:${porta},reuseaddr,fork" "EXEC:sh -c '${comando}',pty,stderr"
}

case "$challenge" in
    G01)
        run_with_socat 7001 "/opt/challenges/bin/hello_compiler"
        ;;
    G02)
        porta="${PORT:-7002}"
        echo "Iniciando G02_legacy_logger na porta ${porta}."
        cd /opt/challenges/G02
        export FLASK_APP=app.main:app
        exec flask run --host=0.0.0.0 --port="${porta}"
        ;;
    G03)
        run_with_socat 7003 "/opt/challenges/bin/symbolic_pointer"
        ;;
    G04)
        run_with_socat 7004 "/opt/challenges/bin/printf_whisper"
        ;;
    G05)
        run_with_socat 7005 "/opt/challenges/bin/compilers_shadow"
        ;;
    A01)
        prepare_python_challenge A01
        run_with_socat 7101 "stdbuf -o0 -e0 python /app/loop.py"
        ;;
    A02)
        prepare_python_challenge A02
        run_with_socat 7102 "stdbuf -o0 -e0 python /app/threads.py"
        ;;
    A03)
        prepare_python_challenge A03
        run_with_socat 7103 "stdbuf -o0 -e0 python /app/scheduler.py"
        ;;
    A04)
        prepare_python_challenge A04
        porta="${PORT:-7104}"
        echo "Iniciando A04_telemetria_sob_sobrecarga na porta ${porta}."
        cd /app
        python monitor.py &
        export FLASK_APP=app:app
        exec flask run --host=0.0.0.0 --port="${porta}"
        ;;
    *)
        echo "Desafio '${challenge}' não é suportado por esta imagem." >&2
        exit 1
        ;;
esac
