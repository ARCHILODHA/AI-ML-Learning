
# K-Nearest Neighbors (KNN)

## Definition

K-Nearest Neighbors is a supervised machine learning algorithm used for classification and regression.

It predicts an observation based on nearby observations.

---

## Basic Idea

For a new data point:

1. Select the value of `K`
2. Calculate distances from existing points
3. Find the K nearest points
4. Use their values to make a prediction

---

## Euclidean Distance

A common distance metric is Euclidean distance:

```text
d = √[(x2-x1)² + (y2-y1)²]
