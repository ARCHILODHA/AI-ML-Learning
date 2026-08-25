# Gradient Boosting

## Definition

Gradient Boosting is an ensemble machine learning technique that builds models sequentially. Each new model attempts to reduce the errors made by the previous models.

Decision trees are commonly used as the weak learners.

## Working

1. Start with an initial prediction.
2. Calculate the errors.
3. Train a weak learner to predict those errors.
4. Add the new model to the existing ensemble.
5. Repeat the process for several iterations.

## Important Hyperparameters

- Learning rate
- Number of estimators
- Maximum tree depth
- Subsample

## Advantages

- High predictive accuracy
- Handles nonlinear relationships
- Works with classification and regression
- Can model complex patterns

## Disadvantages

- Training can be slow
- Sensitive to hyperparameters
- Can overfit if not properly controlled

## Applications

- Fraud detection
- Ranking systems
- Customer prediction
- Financial forecasting
