FROM python:3.11-slim

WORKDIR /aplicacao

COPY . /aplicacao

RUN pip install --no-cache-dir flask==2.3.3

EXPOSE 8083

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
