# Principal Component Analysis (PCA)

## Definition

Principal Component Analysis is a dimensionality reduction technique that transforms a large number of correlated features into a smaller set of uncorrelated features called principal components.

## Main Idea

PCA tries to preserve the maximum possible variance while reducing the number of dimensions.

## Steps

1. Standardize the dataset.
2. Calculate the covariance matrix.
3. Calculate eigenvalues and eigenvectors.
4. Select the principal components with the highest eigenvalues.
5. Transform the original data into the new feature space.

## Advantages

- Reduces dimensionality
- Removes redundant information
- Helps visualization
- Can reduce training time

## Disadvantages

- Principal components may be difficult to interpret
- Sensitive to feature scaling
- Some information may be lost

## Applications

- Data visualization
- Image processing
- Noise reduction
- Feature extraction
