FROM python:3.11-slim

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install flask

ENV FLAG="FLAG{root_32768_001122334466}"

EXPOSE 8080

CMD ["sh", "-c", "echo -n \"$FLAG\" > /flag || true; python app.py"]
