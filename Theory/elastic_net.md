# Elastic Net

## Definition

Elastic Net is a regularization technique that combines L1 and L2 regularization.

It combines the properties of Lasso and Ridge Regression.

## Cost Function

Cost = MSE + λ₁Σ|w| + λ₂Σ(w²)

Where:

- MSE = Mean Squared Error
- λ₁ = L1 regularization strength
- λ₂ = L2 regularization strength
- w = Model coefficients

## Advantages

- Performs feature selection
- Handles correlated features
- Reduces overfitting
- Combines benefits of Lasso and Ridge

## Disadvantages

- Requires tuning multiple parameters
- More complex than ordinary linear regression

## Applications

- High-dimensional datasets
- Feature selection
- Regression problems
- Genomics and text analysis
