FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY app /app
COPY templates /app/templates
COPY static /app/static
COPY config /app/config
COPY data /data

EXPOSE 5000

CMD ["/app/start.sh"]
