import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "age": [20, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "website_visits": [1, 2, 3, 5, 6, 7, 8, 9, 10, 12],
    "time_on_site": [2, 3, 4, 8, 10, 12, 15, 17, 20, 22],
    "purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
})

X = data.drop("purchased", axis=1)
y = data["purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

new_customer = [[28, 6, 9]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Prediction: Customer is likely to purchase")
else:
    print("Prediction: Customer is unlikely to purchase")
