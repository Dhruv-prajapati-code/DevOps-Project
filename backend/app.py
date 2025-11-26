from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
import time
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

start_time = time.time()
REQ_COUNT = Counter("requests_total", "Total HTTP requests", ["path"])

@app.get("/health")
def health():
    REQ_COUNT.labels(path="/health").inc()
    return {"status": "ok", "uptime": round(time.time() - start_time, 2)}

@app.get("/metrics")
def metrics():
    REQ_COUNT.labels(path="/metrics").inc()
    data = generate_latest()
    return PlainTextResponse(data.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)
