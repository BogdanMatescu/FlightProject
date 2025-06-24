FROM python:3.10-buster

RUN apt-get update && \
    apt-get install -y ca-certificates openssl && \
    update-ca-certificates --fresh && \
    ln -sf /etc/ssl/certs/ca-certificates.crt /usr/lib/ssl/cert.pem && \
    apt-get clean

ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

COPY src/ /app/src 

COPY db/ /app/db

COPY static/ app/static  

COPY templates/ app/templates

COPY requirements.txt /app

WORKDIR /app/src

COPY requirements.txt  .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . . 

EXPOSE 5000 

CMD ["python", "main.py"] 

