import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "training_hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12],
    "attendance": [60, 65, 70, 75, 80, 85, 88, 92, 95, 98],
    "projects_completed": [1, 1, 2, 2, 3, 4, 4, 5, 6, 7],
    "performance": [
        "Low",
        "Low",
        "Low",
        "Medium",
        "Medium",
        "Medium",
        "High",
        "High",
        "High",
        "High"
    ]
})

X = data[
    [
        "training_hours",
        "attendance",
        "projects_completed"
    ]
]

y = data["performance"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    "Accuracy:",
    accuracy_score(y_test, predictions)
)

new_employee = [[7, 90, 5]]

prediction = model.predict(new_employee)

print(
    "Predicted Employee Performance:",
    prediction[0]
)
