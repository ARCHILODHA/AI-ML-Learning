# Cross-Validation

## Definition

Cross-validation is a model evaluation technique used to estimate how well a machine learning model will perform on unseen data.

Instead of using only one train-test split, cross-validation divides the dataset into multiple parts and trains/tests the model several times.

---

## K-Fold Cross-Validation

The most common technique is **K-Fold Cross-Validation**.

The dataset is divided into `K` equal-sized folds.

For each iteration:

1. One fold is used for validation.
2. The remaining `K-1` folds are used for training.
3. The process is repeated K times.
4. The evaluation scores are averaged.

### Example

For `K = 5`:

```text
Iteration 1 → Validation: Fold 1
Iteration 2 → Validation: Fold 2
Iteration 3 → Validation: Fold 3
Iteration 4 → Validation: Fold 4
Iteration 5 → Validation: Fold 5
