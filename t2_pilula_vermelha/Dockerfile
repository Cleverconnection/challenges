FROM python:3.11-slim

WORKDIR /aplicacao

COPY . /aplicacao

RUN pip install --no-cache-dir flask==2.3.3

RUN mkdir -p armazenamento

EXPOSE 8081

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
