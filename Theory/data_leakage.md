# Data Leakage in Machine Learning

## Introduction

Data leakage occurs when information unavailable at prediction time
is accidentally used during model training.

It can produce misleadingly high evaluation scores.

## Types of Data Leakage

### 1. Target Leakage

Target leakage occurs when a feature contains information that
directly or indirectly reveals the target variable.

Example:

Using a loan repayment status recorded after loan approval to predict
whether the loan will be repaid.

### 2. Train-Test Contamination

This occurs when information from the test dataset influences
training or preprocessing.

Example:

Calculating normalization statistics using the complete dataset
before splitting it.

### 3. Temporal Leakage

This occurs when future information is used to predict past events.

Example:

Using next month's sales data to predict this month's sales.

## Example of Incorrect Preprocessing

```python
from sklearn.preprocessing import StandardScaler

# Incorrect: fitting on the complete dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting after preprocessing can cause leakage.
```

## Correct Approach

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## Prevention Techniques

- Split data before fitting preprocessing transformations.
- Use pipelines.
- Respect chronological order in time-series problems.
- Remove target-derived features.
- Keep test data isolated.
- Audit feature availability at prediction time.

## Conclusion

Preventing data leakage is essential for obtaining realistic
evaluation results and building reliable machine learning models.
