# Learning Curves in Machine Learning

## Introduction

Learning curves show how model performance changes as the amount
of training data increases.

They help identify overfitting and underfitting.

## Important Components

### Training Score

Measures model performance on training data.

### Validation Score

Measures model performance on unseen validation data.

## Common Patterns

### 1. High Bias

- Training score is low.
- Validation score is also low.
- Both scores may converge at a poor performance level.

Possible solution:

- Increase model complexity.
- Add useful features.
- Reduce excessive regularization.

### 2. High Variance

- Training score is high.
- Validation score is significantly lower.

Possible solution:

- Collect more training data.
- Apply regularization.
- Reduce model complexity.

### 3. Good Generalization

- Training and validation scores are both strong.
- The difference between them is relatively small.

## Python Example

```python
import matplotlib.pyplot as plt

from sklearn.model_selection import learning_curve
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

sizes, train_scores, validation_scores = learning_curve(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy",
    train_sizes=[0.1, 0.3, 0.5, 0.7, 1.0]
)

train_mean = train_scores.mean(axis=1)
validation_mean = validation_scores.mean(axis=1)

plt.plot(sizes, train_mean, marker="o", label="Training Score")
plt.plot(sizes, validation_mean, marker="o", label="Validation Score")

plt.xlabel("Training Examples")
plt.ylabel("Accuracy")
plt.title("Learning Curve")
plt.legend()
plt.grid(True)

plt.show()
```

## Benefits

- Diagnoses bias and variance.
- Helps estimate data requirements.
- Evaluates generalization.
- Supports model improvement.

## Conclusion

Learning curves are useful diagnostic tools for understanding
whether a model needs more data, different features, or adjusted
complexity.
