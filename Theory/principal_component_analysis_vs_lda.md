# PCA vs Linear Discriminant Analysis

## Introduction

PCA and LDA are dimensionality reduction techniques used in machine
learning.

They reduce the number of features while preserving useful information.

## Principal Component Analysis (PCA)

PCA is an unsupervised dimensionality reduction technique.

It identifies directions of maximum variance in the dataset.

### Working Steps

1. Standardize the features.
2. Calculate the covariance matrix.
3. Compute eigenvalues and eigenvectors.
4. Sort components by explained variance.
5. Select the required components.
6. Transform the original dataset.

## Linear Discriminant Analysis (LDA)

LDA is a supervised dimensionality reduction technique.

It finds directions that maximize separation between different classes.

### Working Steps

1. Calculate class-wise means.
2. Calculate within-class scatter.
3. Calculate between-class scatter.
4. Solve the generalized eigenvalue problem.
5. Select discriminant components.
6. Transform the dataset.

## Comparison

| Feature | PCA | LDA |
|---|---|---|
| Learning type | Unsupervised | Supervised |
| Uses labels | No | Yes |
| Objective | Maximum variance | Maximum class separation |
| Applications | Compression | Classification |
| Components | Up to feature count | At most classes - 1 |

## Applications

- Image recognition
- Face recognition
- Pattern classification
- Data visualization
- Feature reduction

## Conclusion

PCA focuses on preserving overall variance, whereas LDA focuses
on separating known classes.
