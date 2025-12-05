FROM python:3.11-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN python /app/init_db.py

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
