# Time Series Forecasting in Machine Learning

## Introduction

Time series forecasting predicts future values using observations
collected over time.

Examples include stock prices, sales, temperature, and demand.

## Components of Time Series

### 1. Trend

Long-term upward or downward movement.

### 2. Seasonality

A repeating pattern occurring at regular intervals.

### 3. Cyclic Patterns

Long-term fluctuations without a fixed repeating period.

### 4. Noise

Random variation that cannot be explained by the model.

## Common Forecasting Methods

| Method | Description |
|---|---|
| Moving Average | Uses averages of recent observations |
| Exponential Smoothing | Gives greater weight to recent observations |
| ARIMA | Models autoregressive and moving-average behavior |
| SARIMA | Extends ARIMA with seasonal components |
| Prophet | Supports trend and seasonality modeling |

## Time-Based Data Splitting

Random splitting is generally unsuitable for forecasting because
it can allow future observations to influence training.

Example:

```python
import pandas as pd

data = pd.read_csv("sales.csv")

data["date"] = pd.to_datetime(data["date"])

data = data.sort_values("date")

split_index = int(len(data) * 0.8)

train = data.iloc[:split_index]
test = data.iloc[split_index:]

print("Training Data:")
print(train.tail())

print("\nTesting Data:")
print(test.head())
```

## Evaluation Metrics

- MAE
- MSE
- RMSE
- MAPE

## Best Practices

- Maintain chronological ordering.
- Check missing timestamps.
- Identify trend and seasonality.
- Avoid future-data leakage.
- Compare against simple baseline forecasts.
- Evaluate on later time periods.

## Conclusion

Time series forecasting is useful for predicting future trends
and supporting data-driven planning and decision-making.
