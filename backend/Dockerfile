FROM python:3.11-alpine

WORKDIR /app

RUN pip install fastapi uvicorn prometheus_client

COPY app.py .
COPY logging.json .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "logging.json"]
