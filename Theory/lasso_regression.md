# Lasso Regression

## Definition

Lasso stands for Least Absolute Shrinkage and Selection Operator. It is a regression technique that uses L1 regularization.

## Cost Function

Cost = MSE + λ × Σ|w|

Where:

- MSE = Mean Squared Error
- λ = Regularization parameter
- w = Model coefficients

## Main Feature

Lasso can shrink some coefficients completely to zero.

Therefore, it can perform automatic feature selection.

## Advantages

- Reduces overfitting
- Performs feature selection
- Useful for high-dimensional datasets
- Produces simpler models

## Disadvantages

- Can struggle when features are highly correlated
- Choice of λ affects performance

## Applications

- Feature selection
- Regression
- High-dimensional machine learning
