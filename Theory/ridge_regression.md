# Ridge Regression

## Definition

Ridge Regression is a linear regression technique that uses L2 regularization to reduce overfitting.

## Cost Function

Ridge Regression adds a penalty term to the ordinary least squares cost function:

Cost = MSE + λ × Σ(w²)

Where:

- MSE = Mean Squared Error
- λ = Regularization parameter
- w = Model coefficients

## Effect of Regularization

As λ increases, model coefficients become smaller.

## Advantages

- Reduces overfitting
- Handles multicollinearity
- Works well when features are correlated

## Disadvantage

Ridge Regression does not usually make coefficients exactly zero, so it does not perform feature selection.

## Applications

- Prediction problems
- High-dimensional datasets
- Datasets with correlated features
