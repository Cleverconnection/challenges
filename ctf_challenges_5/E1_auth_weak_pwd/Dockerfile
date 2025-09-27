FROM python:3.11-slim
WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
RUN pip install flask
ENV FLAG="ITAU2025{weak_passwords_ruin_security}"
ENV FLAG="CTF{placeholder_e1}"
EXPOSE 8080
CMD ["sh", "-c", "echo -n \"$FLAG\" > /flag || true; python app.py"]
