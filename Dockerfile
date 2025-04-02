FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd

COPY wait-for-services.sh /wait-for-services.sh
RUN chmod +x /wait-for-services.sh

EXPOSE 8000
CMD ["/wait-for-db.sh", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
