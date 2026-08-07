# Feature Scaling

## What is Feature Scaling?

Feature scaling transforms numerical features to a common scale so that machine learning algorithms perform better.

## Types

### Standardization

Formula:

Z = (X - Mean) / Standard Deviation

Produces data with mean = 0 and standard deviation = 1.

### Normalization

Formula:

X' = (X - Min) / (Max - Min)

Scales values between 0 and 1.

## Why is it Important?

- Faster model convergence
- Better gradient descent performance
- Prevents features with larger values from dominating

## Algorithms that Need Scaling

- KNN
- SVM
- Logistic Regression
- Neural Networks

## Algorithms that Don't Need Scaling

- Decision Tree
- Random Forest
- XGBoost
