import numpy as np

def train_validation_split(X, y, validation_ratio=0.2):
    X = np.array(X)
    y = np.array(y)

    indices = np.random.permutation(len(X))

    validation_size = int(len(X) * validation_ratio)

    validation_indices = indices[:validation_size]
    train_indices = indices[validation_size:]

    X_train = X[train_indices]
    y_train = y[train_indices]

    X_validation = X[validation_indices]
    y_validation = y[validation_indices]

    return X_train, X_validation, y_train, y_validation


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

y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 1, 0])

X_train, X_validation, y_train, y_validation = train_validation_split(
    X,
    y,
    validation_ratio=0.2
)

print("Training samples:")
print(X_train)

print("\nValidation samples:")
print(X_validation)

print("\nTraining labels:")
print(y_train)

print("\nValidation labels:")
print(y_validation)
