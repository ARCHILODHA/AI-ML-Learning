from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print(
    "Precision:",
    precision_score(
        y_test,
        predictions,
        average="weighted"
    )
)

print(
    "Recall:",
    recall_score(
        y_test,
        predictions,
        average="weighted"
    )
)

print(
    "F1 Score:",
    f1_score(
        y_test,
        predictions,
        average="weighted"
    )
)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
