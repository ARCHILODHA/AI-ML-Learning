# Feature Selection in Machine Learning

## Introduction

Feature selection is the process of selecting the most relevant
features from a dataset.

It improves model efficiency and can reduce overfitting.

## Types of Feature Selection

### 1. Filter Methods

Select features using statistical measurements independently
of a particular predictive model.

Examples:

- Correlation
- Chi-square test
- ANOVA
- Mutual information

### 2. Wrapper Methods

Evaluate different feature subsets using a machine learning model.

Examples:

- Forward selection
- Backward elimination
- Recursive Feature Elimination (RFE)

### 3. Embedded Methods

Perform feature selection during model training.

Examples:

- Lasso regression
- Decision tree feature importance
- Random Forest feature importance

## Python Example Using RFE

```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

selector = RFE(
    estimator=model,
    n_features_to_select=5
)

selector.fit(X_train, y_train)

selected_features = selector.support_

print("Selected Features:")
print(selected_features)

print("\nFeature Rankings:")
print(selector.ranking_)
```

## Benefits

- Reduces dimensionality.
- Improves interpretability.
- Reduces training time.
- Removes irrelevant information.
- May improve generalization.

## Best Practices

- Perform selection using training data only.
- Avoid selecting features using test labels.
- Compare selected and original feature sets.
- Use domain knowledge.
- Validate feature stability.

## Conclusion

Feature selection helps create simpler and more efficient models
by retaining useful information and removing unnecessary features.
