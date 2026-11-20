
import time
from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

app = FastAPI()

PREDICTION_COUNT = Counter(
    "model_prediction_total",
    "Total number of model predictions"
)

PREDICTION_ERRORS = Counter(
    "model_prediction_errors_total",
    "Total number of prediction errors"
)

PREDICTION_LATENCY = Histogram(
    "model_prediction_latency_seconds",
    "Prediction request processing time"
)


@app.get("/")
def home():
    return {"message": "Model monitoring service is running"}


@app.post("/predict")
def predict():
    start_time = time.time()

    try:
        # Replace this section with actual model inference.
        result = {"prediction": 1}

        PREDICTION_COUNT.inc()

        return result

    except Exception:
        PREDICTION_ERRORS.inc()
        raise

    finally:
        PREDICTION_LATENCY.observe(time.time() - start_time)


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain; version=0.0.4"
    )
