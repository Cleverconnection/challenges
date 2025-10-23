FROM python:3.11-slim

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install flask

ENV FLAG="CECYBER{falsa_root_00:11:22:33:44:99}"

EXPOSE 8080

CMD ["sh", "-c", "echo -n \"$FLAG\" > /flag || true; python app.py"]
