FROM python:3.11-slim

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install flask

ENV FLAG="CECYBER{loop_blocked_successfully}"

EXPOSE 8080

CMD ["sh", "-c", "echo -n \"$FLAG\" > /flag || true; python app.py"]
