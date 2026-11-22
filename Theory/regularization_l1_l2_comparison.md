# L1 vs L2 Regularization

## Introduction

Regularization is a technique used to reduce overfitting by adding
a penalty term to the model's loss function.

It discourages unnecessarily large model coefficients.

## L1 Regularization

L1 regularization is also called Lasso regularization.

It adds the absolute values of coefficients to the loss function.

Formula:

```text
Loss = Original Loss + λ Σ|w|
```

Characteristics:

- Can make some coefficients exactly zero.
- Performs automatic feature selection.
- Produces sparse models.

## L2 Regularization

L2 regularization is also called Ridge regularization.

It adds the squared values of coefficients to the loss function.

Formula:

```text
Loss = Original Loss + λ Σw²
```

Characteristics:

- Shrinks coefficient values.
- Usually does not make coefficients exactly zero.
- Helps distribute weights across correlated features.

## Comparison

| Feature | L1 | L2 |
|---|---|---|
| Penalty | Absolute values | Squared values |
| Feature selection | Yes, can produce zeros | Usually no |
| Coefficients | Sparse | Small values |
| Correlated features | May select one | Often distributes weights |
| Common model | Lasso | Ridge |

## Elastic Net

Elastic Net combines L1 and L2 penalties.

```text
Loss = Original Loss
     + λ1 Σ|w|
     + λ2 Σw²
```

## Best Practices

- Standardize numerical features.
- Tune regularization strength.
- Use cross-validation.
- Compare validation performance.
- Avoid excessive regularization.

## Conclusion

L1 is useful for sparse feature selection, while L2 is useful for
controlling large coefficients. Elastic Net combines both approaches.
