#!/bin/sh
set -e
/app/bin/rt_core --help >/dev/null 2>&1 || true
exec python /app/controller.py
