FROM python:3.11-slim
WORKDIR /app
COPY app.py /app/
COPY templates /app/templates
RUN pip install flask
ENV FLAG="ITAU2025{idor_bank_accounts}"
ENV FLAG="CTF{placeholder_e3}"
EXPOSE 8080
CMD ["sh", "-c", "echo -n \"$FLAG\" > /flag || true; python app.py"]
