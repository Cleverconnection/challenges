#!/bin/sh
set -e
python /app/monitor.py &
exec python /app/app.py
