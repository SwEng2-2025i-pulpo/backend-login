from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from app.api.v1 import auth
import time

app = FastAPI()

# Métricas Prometheus
REQUEST_COUNT = Counter(
    "http_requests_total", "Total de peticiones HTTP", ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds", "Duración de la petición en segundos", ["method", "endpoint"]
)

EXCEPTIONS_COUNT = Counter(
    "http_exceptions_total", "Conteo de excepciones por endpoint", ["method", "endpoint"]
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    method = request.method
    endpoint = request.url.path

    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception:
        EXCEPTIONS_COUNT.labels(method=method, endpoint=endpoint).inc()
        status_code = 500
        raise

    duration = time.time() - start_time
    REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=status_code).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)

    return response


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.include_router(auth.router)


# Main entry point for the FastAPI application
# uvicorn app.main:app --reload --port 3003