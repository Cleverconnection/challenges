FROM python:3.11-slim

WORKDIR /aplicacao

COPY . /aplicacao

RUN pip install --no-cache-dir flask==2.3.3

EXPOSE 8080

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
