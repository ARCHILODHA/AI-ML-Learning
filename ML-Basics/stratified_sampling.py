import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40],
    [5, 50],
    [6, 60],
    [7, 70],
    [8, 80],
    [9, 90],
    [10, 100]
])

y = np.array([
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

print("Training labels:")
print(y_train)

print("\nTest labels:")
print(y_test)

print("\nTraining class distribution:")

unique, counts = np.unique(
    y_train,
    return_counts=True
)

for label, count in zip(unique, counts):
    print(label, count)

print("\nTest class distribution:")

unique, counts = np.unique(
    y_test,
    return_counts=True
)

for label, count in zip(unique, counts):
    print(label, count)
