import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "Age": [22, 25, 30, 35, 40, 28, 45, 32, 26, 38],
    "YearsAtCompany": [1, 2, 5, 10, 12, 3, 15, 7, 2, 9],
    "MonthlyIncome": [25000, 30000, 45000, 70000, 85000,
                      35000, 100000, 60000, 28000, 75000],
    "Overtime": [1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    "Attrition": [1, 1, 0, 0, 0, 1, 0, 0, 1, 0]
})

X = data.drop("Attrition", axis=1)
y = data["Attrition"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

employee = [[29, 2, 32000, 1]]
print("Attrition prediction:", model.predict(employee))
