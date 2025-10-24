FROM python:3.11-slim

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install flask gunicorn

ENV FLAG="CTF{falsa_root_00:11:22:33:44:99}"

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
