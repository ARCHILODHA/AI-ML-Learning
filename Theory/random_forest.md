
# Random Forest

## Definition

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to produce a stronger model.

It can be used for classification and regression.

---

## How It Works

Random Forest uses:

1. Multiple training samples
2. Random subsets of features
3. Multiple decision trees
4. Aggregation of predictions

---

## Classification

Each tree makes a prediction.

The final prediction is usually based on majority voting.

```text
Tree 1 → Class A
Tree 2 → Class B
Tree 3 → Class A
Tree 4 → Class A
Tree 5 → Class B

Final → Class A
