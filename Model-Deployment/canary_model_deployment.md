# Canary Model Deployment

## Introduction

Canary deployment is a release strategy in which a new machine learning
model is initially exposed to a small percentage of production traffic.

The remaining traffic continues using the stable model.

## Example Traffic Distribution

| Model | Traffic |
|---|---:|
| Stable Model v1 | 90% |
| New Model v2 | 10% |

## Deployment Workflow

1. Deploy the new model alongside the stable model.
2. Route a small percentage of requests to the new model.
3. Monitor latency, errors, and prediction behavior.
4. Compare the new model against the stable model.
5. Increase traffic gradually if results are acceptable.
6. Route all traffic to the new model after successful validation.
7. Roll back if serious problems occur.

## Example Traffic Routing

```python
import random

def select_model():
    if random.random() < 0.10:
        return "model_v2"

    return "model_v1"
