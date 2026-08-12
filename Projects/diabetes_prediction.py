import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "Glucose": [90, 140, 120, 180, 100, 160, 110, 200],
    "BMI": [22, 30, 25, 35, 24, 32, 26, 38],
    "Age": [25, 45, 30, 55, 28, 50, 35, 60],
    "Diabetes": [0, 1, 0, 1, 0, 1, 0, 1]
})

X = data.drop("Diabetes", axis=1)
y = data["Diabetes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

patient = [[135, 29, 42]]

print("Prediction:", model.predict(patient))
