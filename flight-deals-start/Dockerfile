FROM python:3.12

WORKDIR /app 

COPY reuiremtents.txt 

RUN pip install --no-cache-dir -r requirements.txt 

COPY . . 

EXPOSE 5100 

CMD ["python", "app.py"] 

