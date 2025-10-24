FROM python:3.11-slim

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install flask gunicorn

ENV FLAG="CTF{loop_blocked_successfully}"

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
