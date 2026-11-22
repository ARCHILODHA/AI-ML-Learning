# Class Imbalance in Machine Learning

## Introduction

Class imbalance occurs when one class contains significantly more
observations than another class.

Example:

A fraud detection dataset may contain:

- 9,900 legitimate transactions
- 100 fraudulent transactions

A model predicting every transaction as legitimate would achieve
99% accuracy but fail to identify fraud.

## Problems Caused by Class Imbalance

- Misleading accuracy.
- Poor minority-class recall.
- Biased predictions.
- Difficulty learning rare patterns.

## Handling Techniques

### 1. Random Oversampling

Duplicates minority-class observations to balance the dataset.

### 2. Random Undersampling

Reduces observations from the majority class.

### 3. SMOTE

Synthetic Minority Oversampling Technique creates synthetic
minority-class observations using nearest neighbors.

### 4. Class Weights

Assigns higher penalties to errors involving minority classes.

## Python Example

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))
```

## Important Evaluation Metrics

- Precision
- Recall
- F1-score
- PR-AUC
- ROC-AUC
- Confusion matrix

## Best Practices

- Use stratified splitting.
- Apply resampling only to training data.
- Compare multiple balancing methods.
- Select metrics based on business requirements.
- Evaluate minority-class performance.

## Conclusion

Class imbalance requires careful dataset handling and evaluation.
Accuracy alone is often insufficient for imbalanced classification.
