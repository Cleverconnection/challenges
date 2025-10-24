# syntax=docker/dockerfile:1

FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    FLASK_APP=app.main:app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000
RUN useradd -m hopper
WORKDIR /opt/desafio
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app ./app
COPY data ./data
USER hopper
EXPOSE 5000
CMD ["flask", "run"]
