import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = pd.DataFrame({
    "age": [22, 25, 35, 45, 52, 28, 40, 31, 48, 55],
    "income": [25000, 32000, 50000, 70000, 85000, 30000, 60000, 45000, 75000, 90000],
    "credit_score": [580, 620, 720, 750, 780, 600, 710, 680, 760, 800],
    "debt": [15000, 18000, 10000, 8000, 5000, 20000, 12000, 14000, 7000, 4000],
    "default": [1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
})

X = data.drop("default", axis=1)
y = data["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

new_customer = [[30, 40000, 650, 12000]]

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction[0] == 1:
    print("\nPrediction: Customer may default")
else:
    print("\nPrediction: Customer is unlikely to default")
