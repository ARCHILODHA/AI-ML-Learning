# Model Artifact Management

## Introduction

Model artifacts are files generated during machine learning training.
They may include trained models, preprocessing pipelines, encoders,
tokenizers, and configuration files.

Proper artifact management ensures that deployed applications load
the correct model version.

## Common Artifact Formats

| Format | Usage |
|---|---|
| Pickle | Python object serialization |
| Joblib | Scikit-learn models |
| ONNX | Cross-platform model deployment |
| H5 | Keras models |
| Safetensors | Secure tensor storage |

## Saving a Model

```python
import joblib
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model_v1.joblib")
