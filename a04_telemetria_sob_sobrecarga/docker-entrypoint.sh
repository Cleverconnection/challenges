#!/bin/sh
set -e

ssh-keygen -A >/dev/null 2>&1

if [ -n "$CHALLENGE_CMD" ]; then
  su - player -c "cd /opt/desafio && $CHALLENGE_CMD" &
fi

exec /usr/sbin/sshd -D -e -p "${SSH_PORT:-22}"
